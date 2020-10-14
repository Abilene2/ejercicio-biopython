from Bio import Seq, SeqIO, SeqFeature
from Bio.SeqFeature import SeqFeature, FeatureLocation

def summarize_contents(nombre_archivo):
    print("name: ", nombre_archivo)
    print('path: ...')


    records = list(SeqIO.parse(nombre_archivo,"genbank"))
    print("num_records", len(records))

    print("Records")
    if len(records) == 1 :
        record = SeqIO.read(nombre_archivo, "genbank")
        print("ID: ", record.id)

    else:     
        for seq_record in SeqIO.parse(nombre_archivo, "genbank"):
            print("ID: ", seq_record.id)

