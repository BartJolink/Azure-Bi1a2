import xlrd
from Bio.Blast import NCBIWWW, NCBIXML
import pickle
import mysql.connector

def main():
    ## Executing the blast and parsing the results to a pickle dump file
    sequences, names, scores = get_sequences()
    get_results(sequences, names, scores)


def get_sequences():
    names = []
    sequences = []
    scores = []

    wb = xlrd.open_workbook("Course4_dataset_v03.xlsx")
    sheet = wb.sheet_by_index(13)
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
    for i in range(5): #Change to length of sequences/reads
        sequentie_id = i+1
        print("Currently Blasting: #"+str(sequentie_id))
        print(sequences[i])
        print(names[i])
        blast_record = execute_BLASTx(sequences[i+50])
        titles, accessioncodes, max_scores, query_cover, identities, gaps, \
        organisms, protein_names, sequence_header, lengths, e_values, \
        querys, matches, subjects = create_lists(blast_record)
        dump_results(titles, accessioncodes, max_scores,
                     query_cover, identities, gaps,
                     organisms, protein_names, sequence_header,
                     lengths, e_values,
                     querys, matches, subjects)
        fill_database(sequentie_id, sequences[i], scores[i], names[i])


def execute_BLASTx(seq):
    result_handle = NCBIWWW.qblast("blastx", "nr", seq)

    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    result_handle = open("my_blast.xml")
    blast_record = NCBIXML.read(result_handle)

    return blast_record


def create_lists(blast_record):
    titles, accessioncodes, max_scores, query_cover, identities, gaps,\
    organisms, protein_names, sequence_header, lengths, e_values, \
    querys, matches, subjects = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1.0e-10:
                titles.append(alignment.title)
                accessioncodes.append(alignment.title.split("|")[3])
                max_scores.append(hsp.bits)
                query_cover.append(float((hsp.query_end-hsp.query_start)
                                         /300)*100)
                identities.append((hsp.identities/hsp.align_length)*100)
                gaps.append(hsp.gaps)
                organisms.append(alignment.title.split(">")[0].split("|")
                                 [4].split("[")[1][:-1].strip("]"))
                protein_names.append(alignment.title.split("|")[4]
                                     .split("[")[0][1:])
                lengths.append(alignment.length)
                e_values.append(hsp.expect)
                querys.append(hsp.query)
                matches.append(hsp.match)
                subjects.append(hsp.sbjct)

    return titles, accessioncodes, max_scores, query_cover, identities, \
           gaps, organisms, protein_names, sequence_header, lengths, \
           e_values, querys, matches, subjects


def dump_results(titles, accessioncodes, max_scores, query_cover,
                 identities, gaps, organisms, protein_names,
                 sequence_header, lengths, e_values, querys, matches,
                 subjects):
    filename = "pickle_save_dump"

    with open(filename, 'wb') as f:
        pickle.dump(titles, f)
        pickle.dump(accessioncodes, f)
        pickle.dump(max_scores, f)
        pickle.dump(query_cover, f)
        pickle.dump(identities, f)
        pickle.dump(gaps, f)
        pickle.dump(organisms, f)
        pickle.dump(protein_names, f)
        pickle.dump(sequence_header, f)
        pickle.dump(lengths, f)
        pickle.dump(e_values, f)
        pickle.dump(querys, f)
        pickle.dump(matches, f)
        pickle.dump(subjects, f)

def fill_database(sequentie_id, sequence, score, name):
    filename = "pickle_save_dump"

    with open(filename, 'rb') as f:
        titles = pickle.load(f)
        accessioncodes = pickle.load(f)
        max_scores = pickle.load(f)
        query_cover = pickle.load(f)
        identities = pickle.load(f)
        gaps = pickle.load(f)
        organisms = pickle.load(f)
        protein_names = pickle.load(f)
        sequence_header = pickle.load(f)
        lengths = pickle.load(f)
        e_values = pickle.load(f)
        querys = pickle.load(f)
        matches = pickle.load(f)
        subjects = pickle.load(f)

    password = 'haha1234'

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
                                sequentie_id, lengths[i],organisms[i]))
        SQL_connection.commit()
        cursor.execute(
                        "select * "
                        "from proteine "
                        "where acessiecode like '%{}%';".format(
                            accessioncodes[i]))
        results = cursor.fetchone()
        if results is None:
            cursor.execute("insert into proteine(prot_sequentie, eiwitnaam, acessiecode)"
                       "values('{}', '{}', '{}');".format(subjects[i], protein_names[i], accessioncodes[i]))
            SQL_connection.commit()
        cursor.execute("insert into sequentie(header, nucl_sequentie, score)"
                       "values ('{}', '{}', '{}');".format(name, sequence, score))
        SQL_connection.commit()
        cursor.close()
        SQL_connection.close()

def set_connection(password):
    SQL_connection = mysql.connector.connect(
        host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
        user="ossux@hannl-hlo-bioinformatica-mysqlsrv",
        db="Ossux",
        password=password)


    return SQL_connection


main()