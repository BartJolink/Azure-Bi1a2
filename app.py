from flask import Flask, request
import mysql.connector
import sys

app = Flask(__name__)

def set_connection():
    SQL_connection = mysql.connector.connect(
        host="ensembldb.ensembl.org",
        user="anonymous",
        db="homo_sapiens_core_95_38")

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
                        "select description "
                        "from gene "
                        "where description like '%{}%';".format(
                            searchterm))

        results = cursor.fetchall()
        cursor.close()
        SQL_connection.close()

        formatted_results = ""
        for result in results:
            formatted_results += str(result[0]) + "</br></br>"
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
