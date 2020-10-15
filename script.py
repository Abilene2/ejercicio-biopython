from Bio import SeqIO
import os

def summarize_contents(nombre_archivo):
    print("name: ", nombre_archivo)
    print('path: ', os.path.abspath(nombre_archivo))

    records = list(SeqIO.parse(nombre_archivo,"genbank"))
    print("num_records", len(records))

    print("records: ")
    for seq_record in SeqIO.parse(nombre_archivo, "genbank"):
        print(" - id: ", seq_record.id)
        print("   name: ", seq_record.name)
        print("   description: ", seq_record.description)