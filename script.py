from Bio import SeqIO
import os

def summarize_contents(nombre_archivo):
    resumen = "name: " + nombre_archivo

    resumen += "\npath: " + os.path.abspath(nombre_archivo)

    records = list(SeqIO.parse(nombre_archivo,"genbank"))
    
    resumen += "\nnum_records: " + str(len(records))

    resumen += "\nrecords: "
    for seq_record in SeqIO.parse(nombre_archivo, "genbank"):
        resumen += "\n - id: " + seq_record.id

        resumen += "\n   name: " + seq_record.name

        resumen += "\n   description: " + seq_record.description

    return resumen