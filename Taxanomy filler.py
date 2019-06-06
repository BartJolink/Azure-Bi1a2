## Author: Bart Jolink
## Date: 29-05-2019
## Script for automatic adding taxonomy to Taxonomie database table

from ete3 import NCBITaxa
from Bio import Entrez
import mysql.connector

Entrez.email = 'bart@hotmail.com'

ncbi = NCBITaxa()


def main():
    """"This function directs two functions.
    It takes a password (for database connection) as input.
    """
    
    password = input("Fill in your password: ")
    results = run_query(password)
    organism_names = get_organism_names(results)
    taxids = get_taxids(organism_names)
    fill_taxonomy_database(taxids, password)


def set_connection(password):
    """"This function sets a connection to a database (Ossux).
    (While running, password input was pre-filled. For privacy reasons,
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


def run_query(password):
    """"This function runs a query through the database to check for
    distinct organisms.
    Input is a password to set the connection.
    Output is a query to which gives results to return.
    """

    SQL_connection = set_connection(password)
    cursor = SQL_connection.cursor()
    cursor.execute(
        "select distinct organisme "
        "from blast_resultaten ;")  # limit kan aangepast worden
    results = cursor.fetchall()
    cursor.close()
    SQL_connection.close()

    return results


def get_organism_names(results):
    """"This function creates a list of organism names.
    Input is results (run_query).
    Output is a list; organism_names.
    """

    organism_names = []

    for result in results:
        organism_names.append(result)

    return organism_names


def get_taxids(organism_names):
    """"This function uses Entrez to get the taxonomy ID for each organism in the list.
    Input is a list; organism_names.
    Output is a list of taxids.
    """

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


def fill_taxonomy_database(taxids, password):
    """"This function fills the table Taxonomie in the database Ossux.
    Input is a list of taxids and a password to set the connection.
    Output consists of a query and a commit to the database.
    """

    for taxid in taxids:
        lineage = ncbi.get_lineage(taxid)
        names = ncbi.get_taxid_translator(lineage)
        print(lineage)
        print([names[taxid] for taxid in lineage])

        previous = ""

        for lin in lineage:
            if int(lin) != 1:  # skipping 'root'
                rank = ncbi.get_rank([lin])
                SQL_connection = set_connection(password)
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
                                       "values(NULL, {}, '{}', '{}');".format(
                            lin, names[lin], rank[lin]))
                        SQL_connection.commit()
                    else:
                        cursor.execute("insert into Taxonomie "
                                       "(rank_up, taxonomy_ID, naam, rang) "
                                       "values({}, {}, '{}', '{}');".format(
                            previous, lin, names[lin], rank[lin]))
                        SQL_connection.commit()
                cursor.close()
                SQL_connection.close()
                previous = lin


main()
