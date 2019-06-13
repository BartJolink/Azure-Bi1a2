## Author: Bart Jolink
## Date: 29-05-2019
## Script for automatic blasting of reads of which no results where
# parsed to the database, using tblastx and nr-database.

import xlrd
from Bio.Blast import NCBIWWW, NCBIXML
import mysql.connector
import time


def main():
    """"This function directs two functions.
    """
    
    sequences, names, scores = get_sequences()
    get_results(sequences, names, scores)


def get_sequences():
    """"This function reads a specific worksheet in an Excel file.
    It takes an Excel file with given worksheet-index as input.
    It returns lists for sequences, names and scores
    """
    names = []
    sequences = []
    scores = []

    wb = xlrd.open_workbook("Course4_dataset_v03.xlsx")
    sheet = wb.sheet_by_index(13)  # Index 13 = Worksheet 14
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        names.append(sheet.row_values(i)[0])
        names.append(sheet.row_values(i)[3])
        sequences.append(sheet.row_values(i)[1])
        sequences.append(sheet.row_values(i)[4])
        scores.append(sheet.row_values(i)[2])
        scores.append(sheet.row_values(i)[5])

    return sequences, names, scores


def get_results(sequences, names, scores):
    """"This function directs multiple functions; execute_tBLASTx,
    create_lists and fill_database. After the fill_database function a
    timer of 180 seconds is used to dodge a possible time-out from the
    NCBI servers.
    This function takes all sequences, names and scores (get_sequences)
    as input.
    This function's output is to call functions.
    """

    sequences_blasted = blastcheck()
    blasts_done = 0  # to pick up blasting at a later time..
    for i in range(len(sequences) - blasts_done):
        if int(i + 1 + blasts_done) not in sequences_blasted:
            sequentie_id = i + 1 + blasts_done
            print("Currently Blasting: #" + str(sequentie_id))
            print(sequences[i + blasts_done])
            print(names[i + blasts_done])
            blast_record = execute_tBLASTx(sequences[i + blasts_done])
            titles, accessioncodes, max_scores, query_cover, identities, gaps, \
            organisms, protein_names, sequence_header, lengths, e_values, \
            querys, matches, subjects = create_lists(blast_record)
            fill_database(sequentie_id, sequences[i + blasts_done],
                          scores[i + blasts_done],
                          names[i + blasts_done],
                          titles, accessioncodes, max_scores,
                          query_cover,
                          identities, gaps, organisms, protein_names,
                          lengths, e_values, subjects)
            time.sleep(180)


def execute_tBLASTx(seq):
    """"This function uses NCBIWWW.qblast to perform a tblastx.
     It takes an sequence as input.
     It returns a blast_record as output.
     """

    result_handle = NCBIWWW.qblast("tblastx", "nr", seq)

    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    result_handle = open("my_blast.xml")
    blast_record = NCBIXML.read(result_handle)

    return blast_record


def create_lists(blast_record):
    """"This function parses the information in the blast_record to
    multiple lists. There is an E-value cutoff of 1e-3 and a maximum
    of 10 alignments is safed.
    Input is the blast_record (execute_tBLASTx)
    Output is multiple lists consisting of information about the blast
    results. """

    result_count = 0
    titles, accessioncodes, max_scores, query_cover, identities, gaps, \
    organisms, protein_names, sequence_header, lengths, e_values, \
    querys, matches, subjects = [], [], [], [], [], [], [], [], [], [], [], [], [], []
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if result_count < 10:
                if hsp.expect < 1e-3:
                    titles.append(alignment.title.replace("'", ""))
                    print(alignment.title)
                    accessioncodes.append(alignment.accession)
                    max_scores.append(hsp.bits)
                    query_cover.append(
                        float((hsp.query_end - hsp.query_start)
                              / 300) * 100)
                    identities.append(
                        (hsp.identities / hsp.align_length) * 100)
                    gaps.append(hsp.gaps)
                    if alignment.title[0:2] == 'gi':
                        organisms.append(alignment.title.split(">")[0]
                                         .split("|")[4])
                    else:
                        organisms.append(alignment.title.split(">")[0]
                                         .split("|")[2].split("[")[1]
                                         [:-1].strip("]").replace("'",
                                                                  ""))
                    protein_names.append('full chromosome')
                    lengths.append(alignment.length)
                    e_values.append(hsp.expect)
                    querys.append(hsp.query)
                    matches.append(hsp.match)
                    subjects.append(hsp.sbjct)
                    result_count += 1

    return titles, accessioncodes, max_scores, query_cover, identities, \
           gaps, organisms, protein_names, sequence_header, lengths, \
           e_values, querys, matches, subjects


def fill_database(sequentie_id, sequence, score, name, titles,
                  accessioncodes, max_scores, query_cover, identities,
                  gaps, organisms, protein_names, lengths, e_values,
                  subjects):
    """"This functions fills multiple tables (blast_resultaten,
    proteine, sequentie) within a database (Ossux) with information
    about the blast results. It also checks if a certain acessioncode
    is already existing, to prevent redundancy.
    Input consists of multiple lists with information (create_lists)
    Output consists of multiple commits to fill the database.
    """

    password = input("Fill in your password: ")

    for i in range(len(titles)):
        SQL_connection = set_connection(password)
        cursor = SQL_connection.cursor()
        cursor.execute(
            "insert into blast_resultaten(Title, "
            "acessiecode, E_value, total_score, max_score, "
            "query_cover, perc_identity, gaps, sequentie_id"
            ", length, organisme, blast_id)"
            "values('{}', '{}', '{}', NULL, '{}', '{}'"
            ", '{}', {}, '{}', '{}', '{}', NULL);"
                .format(titles[i], accessioncodes[i],
                        e_values[i], max_scores[i],
                        query_cover[i], identities[i], gaps[i],
                        sequentie_id, lengths[i], organisms[i]))
        SQL_connection.commit()
        cursor.execute(
            "select * "
            "from proteine "
            "where acessiecode like '%{}%';".format(
                accessioncodes[i]))
        results = cursor.fetchone()
        if results is None:
            cursor.execute("insert into proteine(prot_sequentie, "
                           "eiwitnaam, acessiecode)"
                           "values('{}', '{}', '{}');".format(
                subjects[i],
                protein_names[i], accessioncodes[i]))
            SQL_connection.commit()
        cursor.execute(
            "insert into sequentie(header, nucl_sequentie, score)"
            "values ('{}', '{}', '{}');".format(name, sequence, score))
        SQL_connection.commit()
        cursor.close()
        SQL_connection.close()


def blastcheck():
    """"This function checks which distinct sequentie_id are found in
    the database table blast_resultaten.
    Input is a password to connect to the database.
    Output is a list of sequentie_id's of blasted sequences.
    """
    sequences_blasted = []

    password = input("Fill in your password: ")

    SQL_connection = set_connection(password)
    cursor = SQL_connection.cursor()
    cursor.execute(
        "select distinct sequentie_id "
        "from blast_resultaten;")
    results = cursor.fetchall()

    for result in results:
        sequences_blasted.append(result[0])

    return sequences_blasted


def set_connection(password):
    """"This function sets a connection to a database (Ossux).
    (During blasting password input was pre-filled. For privacy reasons,
    the password was changed to an input field)
    Input is a password.
    Output is an SQL_connection.
    """

    SQL_connection = mysql.connector.connect(
        host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
        user="ossux@hannl-hlo-bioinformatica-mysqlsrv",
        db="Ossux",
        password=password)

    return SQL_connection


main()
