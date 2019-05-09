from flask import Flask, request
import re
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML

def DNA_action(text):
    dna_seq = Seq(text.upper())
    transcribe = dna_seq.transcribe()
    translate = dna_seq.translate()

    return """<form method="GET">
    <input name="text">
    <input type="submit">
    <p>Protein sequence: {}
    </form>""".format(translate)


def RNA_action(text):
    rna_seq = Seq(text.upper())
    re_transcribe = rna_seq.back_transcribe()
    translate = rna_seq.translate()

    return """<form method="GET">
    <input name="text">
    <input type="submit">
    <p>Protein sequence: {}
    </form>""".format(translate)


def Protein_action(text):
    blast_record = execute_BLASTp(text)
    title = show_results(blast_record)

    return """<form method="GET">
        <input name="text">
        <input type="submit">
        <p>Protein is likely to be:</br> {}
        </form>""".format(title)

def execute_BLASTp(seq):
    result_handle = NCBIWWW.qblast("blastp", "nr", seq)

    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    result_handle = open("my_blast.xml")
    blast_record = NCBIXML.read(result_handle)

    return blast_record

def show_results(blast_record):
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            title = alignment.title
            break
    return title

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.args.get("text","")
    if bool(re.match('^[ATGCN]', text.upper())) == True:
        return DNA_action(text)
    elif bool(re.match('^[AUGCN]', text.upper())) == True:
        return RNA_action(text)
    elif bool(re.match('^[GALMFWKQESPVICYHRNDT]', text.upper())) == True:
        return Protein_action(text)
    else:
        return """<form method="GET">
            <input name="text">
            <input type="submit">
            <p>Sequence is Invalid!!
            </form>"""





if __name__ == '__main__':
    app.run(debug=True)

