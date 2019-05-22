from ete3 import NCBITaxa
from Bio import Entrez
import mysql.connector

Entrez.email = 'bart@hotmail.com'

ncbi = NCBITaxa()

def main():
    results = run_querry()
    organism_names = get_organism_names(results)
    taxids = get_taxids(organism_names)
    fill_taxonomy_database(taxids)


def set_connection():
    SQL_connection = mysql.connector.connect(
        host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
        user="ossux@hannl-hlo-bioinformatica-mysqlsrv",
        db="Ossux",
        password="haha1234")

    return SQL_connection


def run_querry():
    SQL_connection = set_connection()
    cursor = SQL_connection.cursor()
    cursor.execute(
                    "select distinct organisme "
                    "from blast_resultaten ;") #limit kan aangepast worden
    results = cursor.fetchall()
    cursor.close()
    SQL_connection.close()

    return results


def get_organism_names(results):
    organism_names = []

    for result in results:
        organism_names.append(result)

    return organism_names


def get_taxids(organism_names):
    taxids = []

    for organism in organism_names:
        handle = Entrez.esearch(db="Taxonomy", term=organism)
        record = Entrez.read(handle)
        print(record["IdList"])
        try:
            taxids.append(record["IdList"][0])
        except IndexError:
            pass

    return taxids


def fill_taxonomy_database(taxids):
    for taxid in taxids:
        lineage= ncbi.get_lineage(taxid)
        names = ncbi.get_taxid_translator(lineage)
        print(lineage)
        print([names[taxid] for taxid in lineage])

        previous = ""

        for lin in lineage:
            if int(lin) != 1: #skipping 'root'
                rank = ncbi.get_rank([lin])
                SQL_connection = set_connection()
                cursor = SQL_connection.cursor(buffered=True)
                cursor.execute(
                    "select * "
                    "from Taxonomie "
                    "where taxonomy_ID = {};".format(
                        lin))
                results = cursor.fetchone()
                if results is None:
                    if previous == "":
                        cursor.execute("insert into Taxonomie "
                                       "(rank_up, taxonomy_ID, naam, rang) "
                                       "values(NULL, {}, '{}', '{}');".format(lin, names[lin], rank[lin]))
                        SQL_connection.commit()
                    else:
                        cursor.execute("insert into Taxonomie "
                                       "(rank_up, taxonomy_ID, naam, rang) "
                                       "values({}, {}, '{}', '{}');".format(previous, lin, names[lin], rank[lin]))
                        SQL_connection.commit()
                cursor.close()
                SQL_connection.close()
                previous = lin

    # tree = ncbi.get_topology(taxids)
    # print(tree.get_ascii(attributes=["sci_name", "rank"]))


main()