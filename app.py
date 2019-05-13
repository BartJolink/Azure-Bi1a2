from flask import Flask, request
import mysql.connector
import sys
import re

app = Flask(__name__)

def set_connection():
    SQL_connection = mysql.connector.connect(
        host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
        user="ossux@hannl-hlo-bioinformatica-mysqlsrv",
        db="Ossux",
        password="haha1234")

    return SQL_connection


def run_querry(searchterm, order_by, order):
    try:
        SQL_connection = set_connection()
    except:
        print("Connection failure, please make sure you're connected to "
         "the internet.")
        sys.exit()

    try:
        cursor = SQL_connection.cursor()
        cursor.execute(
                        "select * "
                        "from blast_resultaten "
                        "where Title like '%{}%' "
                        "or acessiecode like '%{}%' "
                        "or organisme like '%{}%'"
                        "order by {} {};".format(
                            searchterm, searchterm, searchterm, order_by, order))

        results = cursor.fetchall()
        cursor.close()
        SQL_connection.close()

        formatted_results = ""
        for result in results:
            for i in result:
                formatted_results += str(i) + '&nbsp;&nbsp;'
            formatted_results += "</br></br>"


        return """<form method="GET">
        <head>Search:</br></head>
        <input name="text"></br>
        <p1>Order by:</p1></br>
        <select name="order_by">
        <option value="Title">Title</option>
        <option value="accessioncode">Accession code</option>
        <option value="e_value">E-value</option>
        <option value="max_score">Max score</option>
        <option value="length">Length</option>
        <option value="organisme">Organism</option>
        <option value="blast_id">Blast_ID</option>
        </select>
        <input type="radio" name="order" value="desc"> Desc
        <input type="radio" name="order" value="asc"> Asc
        </br><br>
        <input type="submit" value="Search">
        <p>Results found:</br> {}
        </form>""".format(formatted_results)

    except:
        return """<form method="GET">
        <head>Search:</br></head>
        <input name="text"></br>
        <p1>Order by:</p1></br>
        <select name="order_by">
        <option value="Title">Title</option>
        <option value="accessioncode">Accession code</option>
        <option value="e_value">E-value</option>
        <option value="max_score">Max score</option>
        <option value="length">Length</option>
        <option value="organisme">Organism</option>
        <option value="blast_id">Blast_ID</option>
        </select>
        <input type="radio" name="order" value="desc"> Desc
        <input type="radio" name="order" value="asc"> Asc
        </br><br>
        <input type="submit" value="Search">
        <p>Results found:</br> 
        </form>"""

@app.route('/', methods=['GET', 'POST'])
def my_form():
    searchterm = request.args.get("text","")
    order_by = request.args.get("order_by", "")
    order = request.args.get("order", "")
    print(order)
    return run_querry(searchterm, order_by, order)

if __name__ == '__main__':
    app.run(debug=True)