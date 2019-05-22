from ete3 import NCBITaxa
from Bio import Entrez
import mysql.connector

Entrez.email = 'bart@hotmail.com'

ncbi = NCBITaxa()

def main():
    results = run_querry()
    organism_names = get_organism_names(results)
    taxids = get_taxids(organism_names)


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

    for organism in organism_names:
        handle = Entrez.esearch(db="Taxonomy", term=organism)
        record = Entrez.read(handle)
        try:
            print(record["IdList"][0], organism[0])
            SQL_connection = set_connection()
            cursor = SQL_connection.cursor(buffered=True)
            cursor.execute(
                "update  Blast_resultaten "
                "set     taxonomy_ID = {} "
                "where organisme = '{}'; ".format(record["IdList"][0], organism[0]))
            SQL_connection.commit()
            cursor.close()
            SQL_connection.close()
        except IndexError:
            pass



    # tree = ncbi.get_topology(taxids)
    # print(tree.get_ascii(attributes=["sci_name", "rank"]))


main()