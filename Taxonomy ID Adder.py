## Author: Bart Jolink
## Date: 29-05-2019
## Script for automatic adding taxonomy to Taxonomie database table.

from ete3 import NCBITaxa
from Bio import Entrez
import mysql.connector

Entrez.email = 'bart@hotmail.com'

ncbi = NCBITaxa()


def main():
    password = input("Fill in your password: ")
    results = run_query(password)
    organism_names = get_organism_names(results)
    get_taxids(organism_names, password)


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


def get_taxids(organism_names, password):
    """"This function uses Entrez to get the taxonomy ID for each
    organism in the list. And update the existing table blast_resultaten.
    Input is a list; organism_names.
    Output is a list of taxids which is used to update the database.
    """

    for organism in organism_names:
        handle = Entrez.esearch(db="Taxonomy", term=organism)
        record = Entrez.read(handle)
        try:
            print(record["IdList"][0], organism[0])
            SQL_connection = set_connection(password)
            cursor = SQL_connection.cursor(buffered=True)
            cursor.execute(
                "update  Blast_resultaten "
                "set     taxonomy_ID = {} "
                "where organisme = '{}'; ".format(record["IdList"][0],
                                                  organism[0]))
            SQL_connection.commit()
            cursor.close()
            SQL_connection.close()
        except IndexError:
            pass


main()
