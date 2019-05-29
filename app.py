html1 = """<!DOCTYPE html>
<html lang="en">
<title>Micro organismen in champost</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, 
initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4
/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/
css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {{font-family: "Poppins", sans-serif}}
body {{font-size:16px;}}
.w3-half img{{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}}
.w3-half img:hover{{opacity:1}}</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large 
w3-padding" style="z-index:3;width:300px;font-weight:bold;" 
id="mySidebar"><br>
<a href="javascript:void(0)" onclick="w3_close()" class=
"w3-button w3-hide-large w3-display-topleft" 
style="width:100%;font-size:22px">Sluit menu</a>
<div class="w3-container">
<h2 class="w3-padding-64"><b>Champost</b></h2>
</div>

<div class="w3-bar-block">
<a href="#" onclick="w3_close()" class="w3-bar-item w3-button 
w3-hover-white">Home</a>
<a href="#informatie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Informatie</a>
<a href="#overzicht" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Overzicht</a>
<a href="#tabel" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Tabel</a>
<a href="#taxonomie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Taxonomie</a>
<a href="#parameters" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Parameters van blast</a>
<a href="#blasten" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Zelf blasten</a>
</div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge 
w3-padding">
<a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" 
onclick="w3_open()">☰</a>
<span>Micro organismen in champost</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" 
style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

<!-- Titel -->
<div class="w3-container" style="margin-top:80px" id="">
<h1 class="w3-jumbo"><b>Micro organismen in champost</b></h1>
  <p>Op deze website is informatie te vinden over champignons
   en over de compost van champignons.
    Ook is er een tabel te vinden met resultaten van het 
    blasten van
      verschillende micro organismen uit de compost van 
      champignons.</p>
</div>

<div class="w3-container" id="informatie" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Informatie</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p> Hieronder is een tabel met verschillende linkjes met 
  informatie over champignons en over de compost van 
  champignons.
    Ook is er een link genaamd 'Blast', dit is de tool die 
    gebruikt is om de resultaten te verkijgen die weergeven
    zijn in een tabel (te vinden bij kopje 'Tabel'). Als u 
    wilt weten wat blasten is, kunt u naar de link 
    'Wikipedia: Blast' of 'NCBI: Blast'.</p>
<div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Informatie
    </li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: 
    Champost </a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: 
    Champignon</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.tuinadvies.nl/artikels/champignons_compost' 
    >Tuinadvies: Champignons compost</a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=
    blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > 
    NCBI: Blast</a></li>
  </ul>
</div>
  <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">
</div>


<!-- Overzicht -->
<div class="w3-container" id="overzicht" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Overzicht</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een pie charm weergegeven over de 10 meest 
voorkomende organismen in de database die is opgezet.
    De database bevat de resultaten van het onderzoek. 
    (meer over het onderzoek bij kopje 'Tabel')</p>
</div>
<head>
<script type="text/javascript">
window.onload = function () {{
var chart = new CanvasJS.Chart("chartContainer",
{{ 
    title:{{ 
        text: "10 Meest voorkomende organismen"
    }},
    legend: {{
        maxWidth: 500,
        itemWidth: 300
    }},
    data: [
    {{
        type: "pie",
        showInLegend: true,
        legendText: "{{ indexLabel}}",
        dataPoints: [
            {{ y: 7, indexLabel: "Escherichia coli" }},
            {{ y: 6, indexLabel: "Proteobacteria bacterium" }},
            {{ y: 6, indexLabel: "Singulisphaera acidiphila" }},
            {{ y: 5, indexLabel: "Mesorhizobium sp"}},
            {{ y: 5, indexLabel: "Xanthomonas oryzae pv. oryzae" }},
            {{ y: 4, indexLabel: "Gammaproteobacteria bacterium"}},
            {{ y: 4, indexLabel: "Myxococcales bacterium"}},
            {{ y: 4, indexLabel: "Thermus thermophilus"}},
            {{ y: 3, indexLabel: "Vulgatibacter incomptus"}},
            {{ y: 3, indexLabel: "Firmicutes bacterium"}}
        ]
    }}
    ]
}});
chart.render();
}}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/
script/canvasjs.min.js"></script>
</head>
<body>
<div id="chartContainer" style="height: 500px; width: 75%;">
</div>
</body>

  <!-- Tabel -->
  <div class="w3-container" id="tabel" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Tabel</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>Hieronder is een tabel weergegeven (als je filtert of zoekt op 
    een zoekwoord). In deze tabel staan de resultaten na het onderzoek 
    met behulp van blasten. </p>
      <p><b>Het onderzoek: </b></p>
    <p>Er is DNA geïsoleerd uit de compost van de champions, deze DNA 
    sequenties zijn in groot excel bestand gezet.
        De sequenties uit dat bestand zijn geblast met behulp van de 
        tool blast (zie kopje parameters of informatie voor meer 
        informatie over blast).
        De resultaten uit de blast zijn opgeslagen in een database, 
        die je hieronder kunt bevragen door te filteren en door op een 
        zoekwoord te zoeken.
        De resultaten komen in de tabel terecht.</p>
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
        <option value="sequentie_id">Sequentie ID</option>
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

    <!-- Taxonomie -->
      <div class="w3-container" id="taxonomie" style="margin-top:75px">
        <h1 class="w3-xxxlarge w3-text-red"><b>Taxonomie</b></h1>
        <hr style="width:50px;border:5px solid red" class="w3-round">
        <p>Hieronder staat een tabel waarmee de taxonomie opgevraagd kan
         worden. </p>
                <form method="GET">
            <head><font face="Poppins">Search:</br></head>
            <input name="text_tax"></br>
            <br><br>
            <input type="submit" value="Search">
            <br><br>
            </form></font>
            </table>
      </div>

  <!-- Parameters -->
  <div class="w3-container" id="parameters" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Parameters van Blast</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p>Hieronder is een tabel weergegeven met de parameters die wij 
      hebben aangepast om zo goed mogelijk en zo betrouwbaar mogelijk 
      resultaat te verkrijgen.</p>
      <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Aangepaste 
        parameters</li>
        <li class="w3-padding-16">Matrix = Blosum 62</li>
        <li class="w3-padding-16">Database = non-redundant protein 
        sequences (nr)</li>
        <li class="w3-padding-16">Word size = 6</li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih
        .gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=
        blasthome'> Blast</a></li>
        <li class="w3-padding-16">De cut-off stond op een e-value van 
        1e-3.</li>
       </ul>
      </div>
      <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
  </div>

<!-- Blasten -->
  <div class="w3-container" id="blasten" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Zelf blasten</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p> Hieronder kunt u zelf een Sequentie invoeren die vervolgens 
      geblast wordt.</p>
      <form method="GET">
        <head><font face="Poppins">Voer een sequentie in:</br></head>
        <input name="blast">
        <input type="submit" value="Blast">
        <br><br>
        </form></font>
        </table>

  </div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" 
style="margin-top:75px;padding-right:58px"><p class="w3-right">
Gemaakt door: Bart Jolink, Wouter Gaykema, Erik Verweij en 
Maite van den Noort</p></div>

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
</html>"""

html2 = """<!DOCTYPE html>
<html lang="en">
<title>Micro organismen in champost</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, 
initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4
/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/
css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {{font-family: "Poppins", sans-serif}}
body {{font-size:16px;}}
.w3-half img{{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}}
.w3-half img:hover{{opacity:1}}</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large 
w3-padding" style="z-index:3;width:300px;font-weight:bold;" 
id="mySidebar"><br>
<a href="javascript:void(0)" onclick="w3_close()" class=
"w3-button w3-hide-large w3-display-topleft" 
style="width:100%;font-size:22px">Sluit menu</a>
<div class="w3-container">
<h2 class="w3-padding-64"><b>Champost</b></h2>
</div>

<div class="w3-bar-block">
<a href="#" onclick="w3_close()" class="w3-bar-item w3-button 
w3-hover-white">Home</a>
<a href="#informatie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Informatie</a>
<a href="#overzicht" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Overzicht</a>
<a href="#tabel" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Tabel</a>
<a href="#taxonomie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Taxonomie</a>
<a href="#parameters" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Parameters van blast</a>
<a href="#blasten" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Zelf blasten</a>
</div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge 
w3-padding">
<a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" 
onclick="w3_open()">☰</a>
<span>Micro organismen in champost</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" 
style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

<!-- Titel -->
<div class="w3-container" style="margin-top:80px" id="">
<h1 class="w3-jumbo"><b>Micro organismen in champost</b></h1>
  <p>Op deze website is informatie te vinden over champignons
   en over de compost van champignons.
    Ook is er een tabel te vinden met resultaten van het 
    blasten van
      verschillende micro organismen uit de compost van 
      champignons.</p>
</div>

<div class="w3-container" id="informatie" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Informatie</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p> Hieronder is een tabel met verschillende linkjes met 
  informatie over champignons en over de compost van 
  champignons.
    Ook is er een link genaamd 'Blast', dit is de tool die 
    gebruikt is om de resultaten te verkijgen die weergeven
    zijn in een tabel (te vinden bij kopje 'Tabel'). Als u 
    wilt weten wat blasten is, kunt u naar de link 
    'Wikipedia: Blast' of 'NCBI: Blast'.</p>
<div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Informatie
    </li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: 
    Champost </a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: 
    Champignon</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.tuinadvies.nl/artikels/champignons_compost' 
    >Tuinadvies: Champignons compost</a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=
    blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > 
    NCBI: Blast</a></li>
  </ul>
</div>
  <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">
</div>


<!-- Overzicht -->
<div class="w3-container" id="overzicht" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Overzicht</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een pie charm weergegeven over de 10 meest 
voorkomende organismen in de database die is opgezet.
    De database bevat de resultaten van het onderzoek. 
    (meer over het onderzoek bij kopje 'Tabel')</p>
</div>
<head>
<script type="text/javascript">
window.onload = function () {{
var chart = new CanvasJS.Chart("chartContainer",
{{ 
    title:{{ 
        text: "10 Meest voorkomende organismen"
    }},
    legend: {{
        maxWidth: 500,
        itemWidth: 300
    }},
    data: [
    {{
        type: "pie",
        showInLegend: true,
        legendText: "{{ indexLabel}}",
        dataPoints: [
            {{ y: 7, indexLabel: "Escherichia coli" }},
            {{ y: 6, indexLabel: "Proteobacteria bacterium" }},
            {{ y: 6, indexLabel: "Singulisphaera acidiphila" }},
            {{ y: 5, indexLabel: "Mesorhizobium sp"}},
            {{ y: 5, indexLabel: "Xanthomonas oryzae pv. oryzae" }},
            {{ y: 4, indexLabel: "Gammaproteobacteria bacterium"}},
            {{ y: 4, indexLabel: "Myxococcales bacterium"}},
            {{ y: 4, indexLabel: "Thermus thermophilus"}},
            {{ y: 3, indexLabel: "Vulgatibacter incomptus"}},
            {{ y: 3, indexLabel: "Firmicutes bacterium"}}
        ]
    }}
    ]
}});
chart.render();
}}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/
script/canvasjs.min.js"></script>
</head>
<body>
<div id="chartContainer" style="height: 500px; width: 75%;">
</div>
</body>

  <!-- Tabel -->
  <div class="w3-container" id="tabel" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Tabel</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>Hieronder is een tabel weergegeven (als je filtert of zoekt op 
    een zoekwoord). In deze tabel staan de resultaten na het onderzoek 
    met behulp van blasten. </p>
      <p><b>Het onderzoek: </b></p>
    <p>Er is DNA geïsoleerd uit de compost van de champions, deze DNA 
    sequenties zijn in groot excel bestand gezet.
        De sequenties uit dat bestand zijn geblast met behulp van de 
        tool blast (zie kopje parameters of informatie voor meer 
        informatie over blast).
        De resultaten uit de blast zijn opgeslagen in een database, 
        die je hieronder kunt bevragen door te filteren en door op een 
        zoekwoord te zoeken.
        De resultaten komen in de tabel terecht.</p>
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
        <option value="sequentie_id">Sequentie ID</option>
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

    <!-- Taxonomie -->
      <div class="w3-container" id="taxonomie" style="margin-top:75px">
        <h1 class="w3-xxxlarge w3-text-red"><b>Taxonomie</b></h1>
        <hr style="width:50px;border:5px solid red" class="w3-round">
        <p>Hieronder staat een tabel waarmee de taxonomie opgevraagd kan
         worden. </p>
                <form method="GET">
            <head><font face="Poppins">Search:</br></head>
            <input name="text_tax"></br>
            <br><br>
            <input type="submit" value="Search">
            <br><br>
            </form></font>
            </table>
      </div>

  <!-- Parameters -->
  <div class="w3-container" id="parameters" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Parameters van Blast</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p>Hieronder is een tabel weergegeven met de parameters die wij 
      hebben aangepast om zo goed mogelijk en zo betrouwbaar mogelijk 
      resultaat te verkrijgen.</p>
      <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Aangepaste 
        parameters</li>
        <li class="w3-padding-16">Matrix = Blosum 62</li>
        <li class="w3-padding-16">Database = non-redundant protein 
        sequences (nr)</li>
        <li class="w3-padding-16">Word size = 6</li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih
        .gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=
        blasthome'> Blast</a></li>
        <li class="w3-padding-16">De cut-off stond op een e-value van 
        1e-3.</li>
       </ul>
      </div>
      <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
  </div>

<!-- Blasten -->
  <div class="w3-container" id="blasten" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Zelf blasten</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p> Hieronder kunt u zelf een Sequentie invoeren die vervolgens 
      geblast wordt.</p>
      <form method="GET">
        <head><font face="Poppins">Voer een sequentie in:</br></head>
        <input name="blast">
        <input type="submit" value="Blast">
        <br><br>
        </form></font>
        </table>

  </div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" 
style="margin-top:75px;padding-right:58px"><p class="w3-right">
Gemaakt door: Bart Jolink, Wouter Gaykema, Erik Verweij en 
Maite van den Noort</p></div>

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
</html>"""

html3 = """<!DOCTYPE html>
<html lang="en">
<title>Micro organismen in champost</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, 
initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4
/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/
css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {{font-family: "Poppins", sans-serif}}
body {{font-size:16px;}}
.w3-half img{{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}}
.w3-half img:hover{{opacity:1}}</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large 
w3-padding" style="z-index:3;width:300px;font-weight:bold;" 
id="mySidebar"><br>
<a href="javascript:void(0)" onclick="w3_close()" class=
"w3-button w3-hide-large w3-display-topleft" 
style="width:100%;font-size:22px">Sluit menu</a>
<div class="w3-container">
<h2 class="w3-padding-64"><b>Champost</b></h2>
</div>

<div class="w3-bar-block">
<a href="#" onclick="w3_close()" class="w3-bar-item w3-button 
w3-hover-white">Home</a>
<a href="#informatie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Informatie</a>
<a href="#overzicht" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Overzicht</a>
<a href="#tabel" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Tabel</a>
<a href="#taxonomie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Taxonomie</a>
<a href="#parameters" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Parameters van blast</a>
<a href="#blasten" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Zelf blasten</a>
</div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge 
w3-padding">
<a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" 
onclick="w3_open()">☰</a>
<span>Micro organismen in champost</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" 
style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

<!-- Titel -->
<div class="w3-container" style="margin-top:80px" id="">
<h1 class="w3-jumbo"><b>Micro organismen in champost</b></h1>
  <p>Op deze website is informatie te vinden over champignons
   en over de compost van champignons.
    Ook is er een tabel te vinden met resultaten van het 
    blasten van
      verschillende micro organismen uit de compost van 
      champignons.</p>
</div>

<div class="w3-container" id="informatie" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Informatie</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p> Hieronder is een tabel met verschillende linkjes met 
  informatie over champignons en over de compost van 
  champignons.
    Ook is er een link genaamd 'Blast', dit is de tool die 
    gebruikt is om de resultaten te verkijgen die weergeven
    zijn in een tabel (te vinden bij kopje 'Tabel'). Als u 
    wilt weten wat blasten is, kunt u naar de link 
    'Wikipedia: Blast' of 'NCBI: Blast'.</p>
<div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Informatie
    </li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: 
    Champost </a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: 
    Champignon</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.tuinadvies.nl/artikels/champignons_compost' 
    >Tuinadvies: Champignons compost</a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=
    blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > 
    NCBI: Blast</a></li>
  </ul>
</div>
  <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">
</div>


<!-- Overzicht -->
<div class="w3-container" id="overzicht" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Overzicht</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een pie charm weergegeven over de 10 meest 
voorkomende organismen in de database die is opgezet.
    De database bevat de resultaten van het onderzoek. 
    (meer over het onderzoek bij kopje 'Tabel')</p>
</div>
<head>
<script type="text/javascript">
window.onload = function () {{
var chart = new CanvasJS.Chart("chartContainer",
{{ 
    title:{{ 
        text: "10 Meest voorkomende organismen"
    }},
    legend: {{
        maxWidth: 500,
        itemWidth: 300
    }},
    data: [
    {{
        type: "pie",
        showInLegend: true,
        legendText: "{{ indexLabel}}",
        dataPoints: [
            {{ y: 7, indexLabel: "Escherichia coli" }},
            {{ y: 6, indexLabel: "Proteobacteria bacterium" }},
            {{ y: 6, indexLabel: "Singulisphaera acidiphila" }},
            {{ y: 5, indexLabel: "Mesorhizobium sp"}},
            {{ y: 5, indexLabel: "Xanthomonas oryzae pv. oryzae" }},
            {{ y: 4, indexLabel: "Gammaproteobacteria bacterium"}},
            {{ y: 4, indexLabel: "Myxococcales bacterium"}},
            {{ y: 4, indexLabel: "Thermus thermophilus"}},
            {{ y: 3, indexLabel: "Vulgatibacter incomptus"}},
            {{ y: 3, indexLabel: "Firmicutes bacterium"}}
        ]
    }}
    ]
}});
chart.render();
}}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/
script/canvasjs.min.js"></script>
</head>
<body>
<div id="chartContainer" style="height: 500px; width: 75%;">
</div>
</body>

  <!-- Tabel -->
  <div class="w3-container" id="tabel" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Tabel</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
    <p>Hieronder is een tabel weergegeven (als je filtert of zoekt op 
    een zoekwoord). In deze tabel staan de resultaten na het onderzoek 
    met behulp van blasten. </p>
      <p><b>Het onderzoek: </b></p>
    <p>Er is DNA geïsoleerd uit de compost van de champions, deze DNA 
    sequenties zijn in groot excel bestand gezet.
        De sequenties uit dat bestand zijn geblast met behulp van de 
        tool blast (zie kopje parameters of informatie voor meer 
        informatie over blast).
        De resultaten uit de blast zijn opgeslagen in een database, 
        die je hieronder kunt bevragen door te filteren en door op een 
        zoekwoord te zoeken.
        De resultaten komen in de tabel terecht.</p>
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
        <option value="sequentie_id">Sequentie ID</option>
        <option value="length">Length</option>
        <option value="organisme">Organism</option>
        </select>
        <input type="radio" name="order" value="asc" checked> Asc<
        <input type="radio" name="order" value="desc"> Desc>
        <br><br>
        <input type="submit" value="Search">
        <br><br>
        </form></font>
        </table>
  </div>

    <!-- Taxonomie -->
      <div class="w3-container" id="taxonomie" style="margin-top:75px">
        <h1 class="w3-xxxlarge w3-text-red"><b>Taxonomie</b></h1>
        <hr style="width:50px;border:5px solid red" class="w3-round">
        <p>Hieronder staat een tabel waarmee de taxonomie opgevraagd kan
         worden. </p>
                <form method="GET">
            <head><font face="Poppins">Search:</br></head>
            <input name="text_tax"></br>
            <br><br>
            <input type="submit" value="Search">
            <p>Meerdere ranks zijn gevonden met jouw zoekopdracht 
            (zie hieronder). Specificeer je zoekopdracht. <p>
            <br>{}
            </form></font>
            </table>
      </div>

  <!-- Parameters -->
  <div class="w3-container" id="parameters" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Parameters van Blast</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p>Hieronder is een tabel weergegeven met de parameters die wij 
      hebben aangepast om zo goed mogelijk en zo betrouwbaar mogelijk 
      resultaat te verkrijgen.</p>
      <div class="w3-half">
      <ul class="w3-ul w3-light-grey w3-center">
        <li class="w3-red w3-xlarge w3-padding-32">Aangepaste 
        parameters</li>
        <li class="w3-padding-16">Matrix = Blosum 62</li>
        <li class="w3-padding-16">Database = non-redundant protein 
        sequences (nr)</li>
        <li class="w3-padding-16">Word size = 6</li>
        <li class="w3-padding-16"><a href = 'https://blast.ncbi.nlm.nih
        .gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=
        blasthome'> Blast</a></li>
        <li class="w3-padding-16">De cut-off stond op een e-value van 
        1e-3.</li>
       </ul>
      </div>
      <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
  </div>

<!-- Blasten -->
  <div class="w3-container" id="blasten" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Zelf blasten</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p> Hieronder kunt u zelf een Sequentie invoeren die vervolgens 
      geblast wordt.</p>
      <form method="GET">
        <head><font face="Poppins">Voer een sequentie in:</br></head>
        <input name="blast">
        <input type="submit" value="Blast">
        <br><br>
        </form></font>
        </table>

  </div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" 
style="margin-top:75px;padding-right:58px"><p class="w3-right">
Gemaakt door: Bart Jolink, Wouter Gaykema, Erik Verweij en 
Maite van den Noort</p></div>

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
</html>"""

html4 = """<!DOCTYPE html>
<html lang="en">
<title>Micro organismen in champost</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, 
initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4
/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/
css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {{font-family: "Poppins", sans-serif}}
body {{font-size:16px;}}
.w3-half img{{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}}
.w3-half img:hover{{opacity:1}}</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large 
w3-padding" style="z-index:3;width:300px;font-weight:bold;" 
id="mySidebar"><br>
<a href="javascript:void(0)" onclick="w3_close()" class=
"w3-button w3-hide-large w3-display-topleft" 
style="width:100%;font-size:22px">Sluit menu</a>
<div class="w3-container">
<h2 class="w3-padding-64"><b>Champost</b></h2>
</div>

<div class="w3-bar-block">
<a href="#" onclick="w3_close()" class="w3-bar-item w3-button 
w3-hover-white">Home</a>
<a href="#informatie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Informatie</a>
<a href="#overzicht" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Overzicht</a>
<a href="#tabel" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Tabel</a>
<a href="#taxonomie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Taxonomie</a>
<a href="#parameters" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Parameters van blast</a>
<a href="#blasten" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Zelf blasten</a>
</div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge 
w3-padding">
<a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" 
onclick="w3_open()">☰</a>
<span>Micro organismen in champost</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" 
style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

<!-- Titel -->
<div class="w3-container" style="margin-top:80px" id="">
<h1 class="w3-jumbo"><b>Micro organismen in champost</b></h1>
  <p>Op deze website is informatie te vinden over champignons
   en over de compost van champignons.
    Ook is er een tabel te vinden met resultaten van het 
    blasten van
      verschillende micro organismen uit de compost van 
      champignons.</p>
</div>

<div class="w3-container" id="informatie" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Informatie</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p> Hieronder is een tabel met verschillende linkjes met 
  informatie over champignons en over de compost van 
  champignons.
    Ook is er een link genaamd 'Blast', dit is de tool die 
    gebruikt is om de resultaten te verkijgen die weergeven
    zijn in een tabel (te vinden bij kopje 'Tabel'). Als u 
    wilt weten wat blasten is, kunt u naar de link 
    'Wikipedia: Blast' of 'NCBI: Blast'.</p>
<div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Informatie
    </li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: 
    Champost </a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: 
    Champignon</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.tuinadvies.nl/artikels/champignons_compost' 
    >Tuinadvies: Champignons compost</a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=
    blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > 
    NCBI: Blast</a></li>
  </ul>
</div>
  <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">
</div>


<!-- Overzicht -->
<div class="w3-container" id="overzicht" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Overzicht</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een pie charm weergegeven over de 10 meest 
voorkomende organismen in de database die is opgezet.
    De database bevat de resultaten van het onderzoek. 
    (meer over het onderzoek bij kopje 'Tabel')</p>
</div>
<head>
<script type="text/javascript">
window.onload = function () {{
var chart = new CanvasJS.Chart("chartContainer",
{{ 
    title:{{ 
        text: "10 Meest voorkomende organismen"
    }},
    legend: {{
        maxWidth: 500,
        itemWidth: 300
    }},
    data: [
    {{
        type: "pie",
        showInLegend: true,
        legendText: "{{ indexLabel}}",
        dataPoints: [
            {{ y: 7, indexLabel: "Escherichia coli" }},
            {{ y: 6, indexLabel: "Proteobacteria bacterium" }},
            {{ y: 6, indexLabel: "Singulisphaera acidiphila" }},
            {{ y: 5, indexLabel: "Mesorhizobium sp"}},
            {{ y: 5, indexLabel: "Xanthomonas oryzae pv. oryzae" }},
            {{ y: 4, indexLabel: "Gammaproteobacteria bacterium"}},
            {{ y: 4, indexLabel: "Myxococcales bacterium"}},
            {{ y: 4, indexLabel: "Thermus thermophilus"}},
            {{ y: 3, indexLabel: "Vulgatibacter incomptus"}},
            {{ y: 3, indexLabel: "Firmicutes bacterium"}}
        ]
    }}
    ]
}});
chart.render();
}}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/
script/canvasjs.min.js"></script>
</head>
<body>
<div id="chartContainer" style="height: 500px; width: 75%;">
</div>
</body>

<!-- Tabel -->
<div class="w3-container" id="tabel" style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Tabel</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een tabel weergegeven (als je filtert of 
zoekt op een zoekwoord). In deze tabel staan de resultaten 
na het onderzoek met behulp van blasten. </p>
  <p><b>Het onderzoek: </b></p>
<p>Er is DNA geïsoleerd uit de compost van de champions, 
deze DNA sequenties zijn in groot excel bestand gezet.
    De sequenties uit dat bestand zijn geblast met behulp 
    van de tool blast (zie kopje parameters of informatie 
    voor meer informatie over blast).
    De resultaten uit de blast zijn opgeslagen in een 
    database, die je hieronder kunt bevragen door te 
    filteren en door op een zoekwoord te zoeken.
    De resultaten komen in de tabel terecht.</p>
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
    <option value="sequentie_id">Sequentie ID</option>
    <option value="length">Length</option>
    <option value="organisme">Organism</option>
    </select>
    <input type="radio" name="order" value="asc" checked> 
    Asc<
    <input type="radio" name="order" value="desc"> 
    Desc>
    <br><br>
    <input type="submit" value="Search">
    <br><br>
    </form></font>
    </table>
</div>

<!-- Taxonomie -->
  <div class="w3-container" id="taxonomie" 
  style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Taxonomie</b></h1>
    <hr style="width:50px;border:5px solid red" 
    class="w3-round">
    <p>Hieronder staat een tabel waarmee de taxonomie 
    opgevraagd kan worden. </p>
            <form method="GET">
        <head><font face="Poppins">Search:</br></head>
        <input name="text_tax"></br>
        <br><br>
        <input type="submit" value="Search">
        <br><br>{}
        </form></font>
        </table>
  </div>

<!-- Parameters -->
<div class="w3-container" id="parameters" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Parameters van Blast
</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p>Hieronder is een tabel weergegeven met de parameters 
  die wij hebben aangepast om zo goed mogelijk en zo 
  betrouwbaar mogelijk resultaat te verkrijgen.</p>
  <div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Aangepaste 
    parameters</li>
    <li class="w3-padding-16">Matrix = Blosum 62</li>
    <li class="w3-padding-16">Database = non-redundant 
    protein sequences (nr)</li>
    <li class="w3-padding-16">Word size = 6</li>
    <li class="w3-padding-16"><a href = 'https://blast.ncbi
    .nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_
    TYPE=BlastSearch&LINK_LOC=blasthome'> Blast</a></li>
    <li class="w3-padding-16">De cut-off stond op een 
    e-value van 1e-3.</li>
   </ul>
  </div>
  <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
</div>

<!-- Blasten -->
<div class="w3-container" id="blasten" style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Zelf blasten</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p> Hieronder kunt u zelf een Sequentie invoeren die 
  vervolgens geblast wordt.</p>
  <form method="GET">
    <head><font face="Poppins">Voer een sequentie in:
    </br></head>
    <input name="blast">
    <input type="submit" value="Blast">
    <br><br>
    </form></font>
    </table>

</div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" 
style="margin-top:75px;padding-right:58px"><p class="w3-right">
Gemaakt door: Bart Jolink, Wouter Gaykema, Erik Verweij en 
Maite van den Noort</p></div>

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
</html>"""

html5 = """<!DOCTYPE html>
<html lang="en">
<title>Micro organismen in champost</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, 
initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4
/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/
css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {{font-family: "Poppins", sans-serif}}
body {{font-size:16px;}}
.w3-half img{{margin-bottom:-6px;margin-top:16px;opacity:0.8;
cursor:pointer}}
.w3-half img:hover{{opacity:1}}
</style>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-red w3-collapse w3-top w3-large 
w3-padding" style="z-index:3;width:300px;font-weight:bold;" 
id="mySidebar"><br>
<a href="javascript:void(0)" onclick="w3_close()" class=
"w3-button w3-hide-large w3-display-topleft" 
style="width:100%;font-size:22px">Sluit menu</a>
<div class="w3-container">
<h2 class="w3-padding-64"><b>Champost</b></h2>
</div>

<div class="w3-bar-block">
<a href="#" onclick="w3_close()" class="w3-bar-item w3-button 
w3-hover-white">Home</a>
<a href="#informatie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Informatie</a>
<a href="#overzicht" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Overzicht</a>
<a href="#tabel" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Tabel</a>
<a href="#taxonomie" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Taxonomie</a>
<a href="#parameters" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Parameters van blast</a>
<a href="#blasten" onclick="w3_close()" class="w3-bar-item 
w3-button w3-hover-white">Zelf blasten</a>
</div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-red w3-xlarge 
w3-padding">
<a href="javascript:void(0)" class="w3-button w3-red w3-margin-right" 
onclick="w3_open()">☰</a>
<span>Micro organismen in champost</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" 
style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

<!-- Titel -->
<div class="w3-container" style="margin-top:80px" id="">
<h1 class="w3-jumbo"><b>Micro organismen in champost</b></h1>
  <p>Op deze website is informatie te vinden over champignons
   en over de compost van champignons.
    Ook is er een tabel te vinden met resultaten van het 
    blasten van
      verschillende micro organismen uit de compost van 
      champignons.</p>
</div>

<div class="w3-container" id="informatie" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Informatie</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p> Hieronder is een tabel met verschillende linkjes met 
  informatie over champignons en over de compost van 
  champignons.
    Ook is er een link genaamd 'Blast', dit is de tool die 
    gebruikt is om de resultaten te verkijgen die weergeven
    zijn in een tabel (te vinden bij kopje 'Tabel'). Als u 
    wilt weten wat blasten is, kunt u naar de link 
    'Wikipedia: Blast' of 'NCBI: Blast'.</p>
<div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Informatie
    </li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champost' >Wikipedia: 
    Champost </a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/Champignon' > Wikipedia: 
    Champignon</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.tuinadvies.nl/artikels/champignons_compost' 
    >Tuinadvies: Champignons compost</a></li>
    <li class="w3-padding-16"><a href = 
    'https://nl.wikipedia.org/wiki/BLAST'> Wikipedia: 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=
    blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'> 
    Blast</a></li>
    <li class="w3-padding-16"><a href = 
    'https://www.ncbi.nlm.nih.gov/pubmed/22708584' > 
    NCBI: Blast</a></li>
  </ul>
</div>
  <img src=" https://media1.tenor.com/images/26799fe5136a8186d7d2dbb121b726a5/tenor.gif?itemid=13655817">
</div>


<!-- Overzicht -->
<div class="w3-container" id="overzicht" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Overzicht</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een pie charm weergegeven over de 10 meest 
voorkomende organismen in de database die is opgezet.
    De database bevat de resultaten van het onderzoek. 
    (meer over het onderzoek bij kopje 'Tabel')</p>
</div>
<head>
<script type="text/javascript">
window.onload = function () {{
var chart = new CanvasJS.Chart("chartContainer",
{{ 
    title:{{ 
        text: "10 Meest voorkomende organismen"
    }},
    legend: {{
        maxWidth: 500,
        itemWidth: 300
    }},
    data: [
    {{
        type: "pie",
        showInLegend: true,
        legendText: "{{ indexLabel}}",
        dataPoints: [
            {{ y: 7, indexLabel: "Escherichia coli" }},
            {{ y: 6, indexLabel: "Proteobacteria bacterium" }},
            {{ y: 6, indexLabel: "Singulisphaera acidiphila" }},
            {{ y: 5, indexLabel: "Mesorhizobium sp"}},
            {{ y: 5, indexLabel: "Xanthomonas oryzae pv. oryzae" }},
            {{ y: 4, indexLabel: "Gammaproteobacteria bacterium"}},
            {{ y: 4, indexLabel: "Myxococcales bacterium"}},
            {{ y: 4, indexLabel: "Thermus thermophilus"}},
            {{ y: 3, indexLabel: "Vulgatibacter incomptus"}},
            {{ y: 3, indexLabel: "Firmicutes bacterium"}}
        ]
    }}
    ]
}});
chart.render();
}}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/
script/canvasjs.min.js"></script>
</head>
<body>
<div id="chartContainer" style="height: 500px; width: 75%;">
</div>
</body>

<!-- Tabel -->
<div class="w3-container" id="tabel" style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Tabel</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
<p>Hieronder is een tabel weergegeven (als je filtert of 
zoekt op een zoekwoord). In deze tabel staan de resultaten 
na het onderzoek met behulp van blasten. </p>
  <p><b>Het onderzoek: </b></p>
<p>Er is DNA geïsoleerd uit de compost van de champions, 
deze DNA sequenties zijn in groot excel bestand gezet.
    De sequenties uit dat bestand zijn geblast met behulp 
    van de tool blast (zie kopje parameters of informatie 
    voor meer informatie over blast).
    De resultaten uit de blast zijn opgeslagen in een 
    database, die je hieronder kunt bevragen door te 
    filteren en door op een zoekwoord te zoeken.
    De resultaten komen in de tabel terecht.</p>
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
    <option value="sequentie_id">Sequentie ID</option>
    <option value="length">Length</option>
    <option value="organisme">Organism</option>
    </select>
    <input type="radio" name="order" value="asc" checked> 
    Asc<
    <input type="radio" name="order" value="desc"> 
    Desc>
    <br><br>
    <input type="submit" value="Search">
    <br><br>
    </form></font>
    </table>
</div>

<!-- Taxonomie -->
  <div class="w3-container" id="taxonomie" 
  style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Taxonomie</b></h1>
    <hr style="width:50px;border:5px solid red" 
    class="w3-round">
    <p>Hieronder staat een tabel waarmee de taxonomie 
    opgevraagd kan worden. </p>
            <form method="GET">
        <head><font face="Poppins">Search:</br></head>
        <input name="text_tax"></br>
        <br><br>
        <input type="submit" value="Search">
        <br><br>
        </form></font>
        </table>
  </div>

<!-- Parameters -->
<div class="w3-container" id="parameters" 
style="margin-top:75px">
<h1 class="w3-xxxlarge w3-text-red"><b>Parameters van Blast
</b></h1>
<hr style="width:50px;border:5px solid red" class="w3-round">
  <p>Hieronder is een tabel weergegeven met de parameters 
  die wij hebben aangepast om zo goed mogelijk en zo 
  betrouwbaar mogelijk resultaat te verkrijgen.</p>
  <div class="w3-half">
  <ul class="w3-ul w3-light-grey w3-center">
    <li class="w3-red w3-xlarge w3-padding-32">Aangepaste 
    parameters</li>
    <li class="w3-padding-16">Matrix = Blosum 62</li>
    <li class="w3-padding-16">Database = non-redundant 
    protein sequences (nr)</li>
    <li class="w3-padding-16">Word size = 6</li>
    <li class="w3-padding-16"><a href = 'https://blast.ncbi
    .nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_
    TYPE=BlastSearch&LINK_LOC=blasthome'> Blast</a></li>
    <li class="w3-padding-16">De cut-off stond op een 
    e-value van 1e-3.</li>
   </ul>
  </div>
  <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif">
</div>

<!-- Blasten -->
  <div class="w3-container" id="blasten" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-red"><b>Zelf blasten</b></h1>
    <hr style="width:50px;border:5px solid red" class="w3-round">
      <p> Hieronder kunt u zelf een Sequentie invoeren die vervolgens 
      geblast wordt.</p>
      <form method="GET">
        <head><font face="Poppins">Voer een sequentie in:</br></head>
        <input name="blast">
        <input type="submit" value="Blast">
        {}
        <br><br>
        </form></font>
        </table>

  </div>

<!-- End page content -->
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" style="margin-top:
75px;padding-right:58px"><p class="w3-right">Gemaakt door: Bart Jolink, 
Wouter Gaykema, Erik Verweij en Maite van den Noort</p></div>

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
</html>"""

# Hier begint de code

from flask import Flask, request, render_template, url_for
import mysql.connector
import sys
import re
from Bio.Blast import NCBIWWW, NCBIXML

app = Flask(__name__)


def set_connection():
    SQL_connection = mysql.connector.connect(
        host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
        user="ossux@hannl-hlo-bioinformatica-mysqlsrv",
        db="Ossux",
        password="haha1234")

    return SQL_connection


def run_querry(searchterm, order_by, order, html1, html2):
    try:
        SQL_connection = set_connection()
    except:
        print("Connection failure, please make sure you're connected to"
              " the internet.")
        sys.exit()
    try:
        formatted_table = ""
        cursor = SQL_connection.cursor()
        cursor.execute(
            "select * "
            "from blast_resultaten "
            "where Title like '%{}%' "
            "or acessiecode like '%{}%' "
            "or organisme like '%{}%'"
            "order by {} {};".format(
                searchterm, searchterm, searchterm,
                order_by, order))

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
                "<th>Taxonomy_ID</th>" \
                " </tr>"

        formatted_table = table
        for result in results:
            formatted_table += "<tr bgcolor='#f1f1f1'>"
            for i in result:
                formatted_table += "<td>" + str(i) + "</td>"
            formatted_table += "</tr>"

        return html1.format(formatted_table)
    except:
        return html2.format(formatted_table)


def run_taxonomy(searchterm, html3, html4):
    try:
        SQL_connection = set_connection()
    except:
        print(
            "Connection failure, please make sure you're connected to "
            "the internet.")
        sys.exit()
    try:
        table = "<table>" \
                "<tr bgcolor='#f44336'>" \
                "<th>Organism</th>" \
                "<th>Rank</th>" \
                " </tr>"
        cursor = SQL_connection.cursor()
        cursor.execute(
            "select * "
            "from Taxonomie "
            "where naam like '%{}%'; ".format(searchterm))
        results = cursor.fetchall()
        cursor.close()
        SQL_connection.close()
        print(results)
        if len(results) > 1:
            formatted_table = table
            "<tr bgcolor='#f1f1f1'>"
            for result in results:
                formatted_table += "<tr bgcolor='#f1f1f1'>"
                for i in range(len(result)):
                    if i > 1:
                        formatted_table += "<td>" + str(result[i]) \
                                           + "</td>"
                formatted_table += "</tr>"

            return html3.format(formatted_table)

        print(results[0])
        table = "<table>" \
                "<tr bgcolor='#f44336'>" \
                "<th>Rank-up</th>" \
                "<th>Taxonomy_ID</th>" \
                "<th>Name</th>" \
                "<th>Rank</th>" \
                " </tr>"

        formatted_table = table
        taxids = []

        while results[0][1] != 131567:
            next_tax = results[0][0]
            taxids.append(results[0][0])
            print(next_tax)
            for result in results:
                formatted_table += "<tr bgcolor='#f1f1f1'>"
                for i in result:
                    formatted_table += "<td>" + str(i) + "</td>"
                formatted_table += "</tr>"

            SQL_connection = set_connection()
            cursor = SQL_connection.cursor()
            print(next_tax)
            cursor.execute(
                "select * "
                "from Taxonomie "
                "where taxonomy_ID = {}; ".format(next_tax))
            results = cursor.fetchall()
            cursor.close()
            SQL_connection.close()
            print(results[0][0])

        return html4.format(formatted_table)
    except:
        pass


def execute_BLASTp(seq):
    result_handle = NCBIWWW.qblast("blastp", "nr", seq)
    ## rechten azure file verhogen.
    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    result_handle = open("my_blast.xml")
    blast_record = NCBIXML.read(result_handle)

    return blast_record


def show_results(blast_record):
    results = []
    counter = 0
    for alignment in blast_record.alignments:
        if counter < 5:
            for hsp in alignment.hsps:
                results.append("***Alignment***")
                results.append("sequence:" + str(alignment.title))
                results.append("length:" + str(alignment.length))
                results.append("e value:" + str(hsp.expect))
                results.append(str(hsp.query[0:75]) + "...")
                results.append(str(hsp.match[0:75]) + "...")
                results.append(str(hsp.sbjct[0:75]) + "...")
                results.append("<br>")
                counter += 1
    return results


def run_blast(blast, html5):
    blast_record = execute_BLASTp(blast)
    results = show_results(blast_record)

    formatted_results = "Blasts results:<br>"
    for result in results:
        formatted_results += str(result) + '<br>'

    return html5.format(formatted_results)


@app.route('/', methods=['GET'])
def my_form():
    searchterm = request.args.get("text", "")
    order_by = request.args.get("order_by", "")
    order = request.args.get("order", "")
    taxonomie = request.args.get("text_tax", "")
    tax_choice = request.args.get("tax", "")
    blast = request.args.get("blast", "")

    if blast != "":
        return run_blast(blast, html5)
    if taxonomie != "":
        return run_taxonomy(taxonomie, html3, html4)
    else:
        return run_querry(searchterm, order_by, order, html1, html2)


if __name__ == '__main__':
    app.run(debug=True)
