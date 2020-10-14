from Bio import SeqIO, SeqFeature
from Bio.SeqFeature import SeqFeature, FeatureLocation
import os

nomArchivo = "ls_orchid.gbk"

def summarize_contents(nombre_archivo):
    print("name: ", nombre_archivo)
    print('path: ', os.path.dirname(nombre_archivo))

    records = list(SeqIO.parse(nombre_archivo,"genbank"))
    print("num_records", len(records))

    for seq_record in SeqIO.parse(nombre_archivo, "genbank"):
        print("name: ", seq_record.name)
        print("ID: ", seq_record.id)
        print("location: ")
        for seq_features in seq_record.features:
            print("start: %d, stop %d"%(int(seq_features.location.start),int(seq_features.location.end)))

summarize_contents(nomArchivo)

