from Bio import SeqIO, SeqRecord
def summarize_contents(nom_archivo):
    record = SeqIO.read(nom_archivo, "genbank") 
    print("name:")
    print(nom_archivo)
    