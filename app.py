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


def run_querry(searchterm):
    try:
        SQL_connection = set_connection()
    except:
        print("Connection failure, please make sure you're connected to "
         "the internet.")
        sys.exit()

    if searchterm != "":
        cursor = SQL_connection.cursor()
        cursor.execute(
                        "select *"
                        "from blast_resultaten"
                        "where Title like '{}'"
                        "or acessiecode like '{}'"
                        "or organisme like '{}';".format(
                            searchterm, searchterm, searchterm))

        results = cursor.fetchall()
        cursor.close()
        SQL_connection.close()

        formatted_results = ""
        for result in results:
            index = re.search(searchterm.upper(), result[0].upper())
            if index is None:
                formatted_results += str(result[0]) + "</br></br>"
            else:
                index = index.start()
                print(index)
                formatted_results += str(result[0][0:index])+'<b><font color="red">'+str(result[0][index:index+len(searchterm)])+"</b></font>"+str(result[0][index+len(searchterm):]) + "</br></br>"
    else:
        formatted_results = ""

    return """<form method="GET">
    <head>Fill in your searchterm</br></head>
    <input name="text">
    <input type="submit">
    <p>Results found:</br> {}
    </form>""".format(formatted_results)

@app.route('/', methods=['GET', 'POST'])
def my_form():
    searchterm = request.args.get("text","")
    return run_querry(searchterm)

if __name__ == '__main__':
    app.run(debug=True)