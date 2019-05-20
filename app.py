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
        formatted_table = "sdafsdf"
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

        table = "<table>" \
                "<tr bgcolor='#f44336'>" \
                "<th>Title</th>" \
                "<th>Accessioncode</th>" \
                "<th>E-value</th>" \
                "<th>Total score</th>" \
                "<th>Max score</th>" \
                "<th>Query cover</th>" \
                "<th>Identities</th>" \
                "<th>Gaps</th>" \
                "<th>Sequentie ID</th>" \
                "<th>Length</th>" \
                "<th>Organism</th>" \
                "<th>Blast_ID</th>" \
                " </tr>" \

        formatted_table = table
        for result in results:
            formatted_table += "<tr bgcolor='#f1f1f1'>"
            for i in result:
                formatted_table += "<td>" + str(i) + "</td>"
            formatted_table += "</tr>"

        print(formatted_table)




        return """<!DOCTYPE html>
<html lang="en">
<title>blok 4 groepje 3, aanpassen</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {{font-family: "Poppins", sans-serif}}
body {{font-size:16px;}}
.w3-half img{{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}}
.w3-half img:hover{{opacity:1}}
</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large w3-padding" style="z-index:3;width:300px;font-weight:bold;" id="mySidebar"><br>
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-button w3-hide-large w3-display-topleft" style="width:100%;font-size:22px">Close Menu</a>
  <div class="w3-container">
    <h3 class="w3-padding-64"><b>Championen<br>compost</b></h3>

  </div>
  <div class="w3-bar-block">
    <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Home</a>
    <a href="#showcase" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Informatie</a>
    <a href="#services" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Overzicht</a>
    <a href="#designers" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Tabel</a>
    <a href="#packages" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Parameters van blast</a>
    <!--<a href="#contact" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">miss straks nodig</a> -->
  </div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge w3-padding">
  <a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" onclick="w3_open()">☰</a>
  <span>Company Name</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

  <!-- Header -->
  <div class="w3-container" style="margin-top:80px" id="showcase">
    <h1 class="w3-jumbo"><b>titel</b></h1>
      <p>Op deze website is informatie te vinden over champignons en over de compost van champignons.
        Ook is er een tabel te vinden met resultaten van het blasten van
          verschillende micro organismen uit de compost van champignons.</p>
      <img src= 'https://media.giphy.com/media/bSEkPdQfsSHCMYn7fD/giphy.gif'>
    <h1 class="w3-xxxlarge w3-text-red"><b>informatie</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
  </div>

    <p> Hieronder is een tabel met verschillende linkjes met informatie over de boven genoemde onderwerpen.
        Ook is er een link genaamd 'Blast', dit is de tool die gebruikt is om de resultaten te verkijgen die weergeven
        zijn in een tabel (te vinden bij kopje 'Tabel'). Als u wilt weten wat blasten is, kunt u naar de link 'Wikipedia: Blast' of 'NCBI: Blast'.</p>
    <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Informatie</li>
        <li class="w3-padding-16"><a href = 'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: Champost </a></li>
        <li class="w3-padding-16"><a href = 'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: Champignon</a></li>
        <li class="w3-padding-16"><a href = 'https://www.tuinadvies.nl/artikels/champignons_compost' >Tuinadvies: Champignons compost</a></li>
        <li class="w3-padding-16"><a href = 'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: Blast</a></li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> Blast</a></li>
        <li class="w3-padding-16"><a href = 'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > NCBI: Blast</a></li>
      </ul>
    </div>
    <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">

  <!-- Services -->
  <div class="w3-container" id="services" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>overzicht.</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>hier moet een kort overzichtje komen over de 5 meest gevonden resultaten en of het logisch is dat we dit hebben gevonden.</p>
    <p>hier komt het stukje tekst (eventueel het gekaraktisereerde eiwit)
            zit niet op de zelfde lijn met de rest van de tekst???</p>
      

  <!-- Designers -->
  <div class="w3-container" id="designers" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>tabel.</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>hier omt de titel en korte beschrijving van de tabel.</p>
    <p>hier komt de tabel als overzicht van alle blast resultaten met filters die je kan aan vinken.</p>
      <form method="GET">
        <head><font face="Poppins">Search:</br></head>
        <input name="text"></br>
        <p1>Order by:</p1></br>
        <select name="order_by">
        <option value="blast_id">Blast_ID</option>
        <option value="Title">Title</option>
        <option value="acessiecode">Accession code</option>
        <option value="e_value">E-value</option>
        <option value="max_score">Max score</option>
        <option value="query_cover">Query cover</option>
        <option value="perc_identity">Identity %</option>
        <option value="length">Length</option>
        <option value="organisme">Organism</option>
        </select>
        <input type="radio" name="order" value="asc" checked> Asc<
        <input type="radio" name="order" value="desc"> Desc>
        <br><br>
        <input type="submit" value="Search">
        <br><br>{}
        </form></font>
        </table>
  </div>

  <!-- Packages / Pricing Tables -->
  <div class="w3-container" id="packages" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>parameter van blast.</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p>Hier onder is een tabel weergegeven met de parameters die wij hebben aangepast om zo goed mogelijk en zo betrouwbaar mogelijk resultaat te verkrijgen.</p>
      <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Aangepaste parameters</li>
        <li class="w3-padding-16">Matrix = Blosum 62</li>
        <li class="w3-padding-16">Database = non-redundant protein sequences (nr)</li>
        <li class="w3-padding-16">Word size = 6</li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> Blast</a></li>
       </ul>
      <p> Ook is er een cut off ingesteld op een e-value van 3e. </p>
    </div>
      <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
  </div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" style="margin-top:75px;padding-right:58px"><p class="w3-right">gemaakt door<a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-opacity">Erik, Wouter, Bart en Maite :)</a></p></div>

<script>
// Script to open and close sidebar
function w3_open() {{
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}}

function w3_close() {{
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}}

// Modal Image Gallery
function onClick(element) {{
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}}
</script>

</body>
</html>""".format(formatted_table)

    except:
        return """"<!DOCTYPE html>
<html lang="en">
<title>blok 4 groepje 3, aanpassen</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif}
body {font-size:16px;}
.w3-half img{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}
.w3-half img:hover{opacity:1}
</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large w3-padding" style="z-index:3;width:300px;font-weight:bold;" id="mySidebar"><br>
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-button w3-hide-large w3-display-topleft" style="width:100%;font-size:22px">Close Menu</a>
  <div class="w3-container">
    <h3 class="w3-padding-64"><b>Championen<br>compost</b></h3>

  </div>
  <div class="w3-bar-block">
    <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Home</a>
    <a href="#showcase" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Informatie</a>
    <a href="#services" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Overzicht</a>
    <a href="#designers" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Tabel</a>
    <a href="#packages" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Parameters van blast</a>
    <!--<a href="#contact" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">miss straks nodig</a> -->
  </div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge w3-padding">
  <a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" onclick="w3_open()">☰</a>
  <span>Company Name</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

  <!-- Header -->
  <div class="w3-container" style="margin-top:80px" id="showcase">
    <h1 class="w3-jumbo"><b>titel</b></h1>
      <p>Op deze website is informatie te vinden over champignons en over de compost van champignons.
        Ook is er een tabel te vinden met resultaten van het blasten van
          verschillende micro organismen uit de compost van champignons.</p>
      <img src= 'https://media.giphy.com/media/bSEkPdQfsSHCMYn7fD/giphy.gif'>
    <h1 class="w3-xxxlarge w3-text-red"><b>informatie</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
  </div>

    <p> Hieronder is een tabel met verschillende linkjes met informatie over de boven genoemde onderwerpen.
        Ook is er een link genaamd 'Blast', dit is de tool die gebruikt is om de resultaten te verkijgen die weergeven
        zijn in een tabel (te vinden bij kopje 'Tabel'). Als u wilt weten wat blasten is, kunt u naar de link 'Wikipedia: Blast' of 'NCBI: Blast'.</p>
    <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Informatie</li>
        <li class="w3-padding-16"><a href = 'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: Champost </a></li>
        <li class="w3-padding-16"><a href = 'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: Champignon</a></li>
        <li class="w3-padding-16"><a href = 'https://www.tuinadvies.nl/artikels/champignons_compost' >Tuinadvies: Champignons compost</a></li>
        <li class="w3-padding-16"><a href = 'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: Blast</a></li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> Blast</a></li>
        <li class="w3-padding-16"><a href = 'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > NCBI: Blast</a></li>
      </ul>
    </div>
    <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">

  <!-- Services -->
  <div class="w3-container" id="services" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>overzicht.</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>hier moet een kort overzichtje komen over de 5 meest gevonden resultaten en of het logisch is dat we dit hebben gevonden.</p>
    <p>hier komt het stukje tekst (eventueel het gekaraktisereerde eiwit)
            zit niet op de zelfde lijn met de rest van de tekst???</p>


  <!-- Designers -->
  <div class="w3-container" id="designers" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>tabel.</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>hier omt de titel en korte beschrijving van de tabel.</p>
    <p>hier komt de tabel als overzicht van alle blast resultaten met filters die je kan aan vinken.</p>
      <form method="GET">
        <head><font face="Poppins">Search:</br></head>
        <input name="text"></br>
        <p1>Order by:</p1></br>
        <select name="order_by">
        <option value="blast_id">Blast_ID</option>
        <option value="Title">Title</option>
        <option value="acessiecode">Accession code</option>
        <option value="e_value">E-value</option>
        <option value="max_score">Max score</option>
        <option value="query_cover">Query cover</option>
        <option value="perc_identity">Identity %</option>
        <option value="length">Length</option>
        <option value="organisme">Organism</option>
        </select>
        <input type="radio" name="order" value="asc" checked> Asc>
        <input type="radio" name="order" value="desc"> Desc>
        </br><br>
        <input type="submit" value="Search">
        </form>
        </br></font>
        </table>
  </div>

  <!-- Packages / Pricing Tables -->
  <div class="w3-container" id="packages" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>parameter van blast.</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p>Hier onder is een tabel weergegeven met de parameters die wij hebben aangepast om zo goed mogelijk en zo betrouwbaar mogelijk resultaat te verkrijgen.</p>
      <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Aangepaste parameters</li>
        <li class="w3-padding-16">Matrix = Blosum 62</li>
        <li class="w3-padding-16">Database = non-redundant protein sequences (nr)</li>
        <li class="w3-padding-16">Word size = 6</li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> Blast</a></li>
       </ul>
      <p> Ook is er een cut off ingesteld op een e-value van 3e. </p>
    </div>
      <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
  </div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" style="margin-top:75px;padding-right:58px"><p class="w3-right">gemaakt door<a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-opacity">Erik, Wouter, Bart en Maite :)</a></p></div>

<script>
// Script to open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}
</script>

</body>
</html>"""

@app.route('/', methods=['GET'])
def my_form():
    searchterm = request.args.get("text", "")
    order_by = request.args.get("order_by", "")
    order = request.args.get("order", "")
    return run_querry(searchterm, order_by, order)

if __name__ == '__main__':
    app.run(debug=True)