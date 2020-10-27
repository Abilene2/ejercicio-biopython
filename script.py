from Bio import SeqIO
import os

archivo = os.path.abspath("AF323668.gbk")

def summarize_contents (nombre_archivo):
    listaOs = os.path.split(nombre_archivo)
    listaExt = os.path.splitext(nombre_archivo)
    
    if listaExt[1] == ".gbk":
        tipoArchivo = "genbank"
    else:
        tipoArchivo = "fasta"
    

    record = list(SeqIO.parse(nombre_archivo,tipoArchivo))

    #Creacion del diccionario 
    d = {}
    
    d['File:'] = listaOs[1]
    d['Path:'] = listaOs[0]
    
    d['Num_records:'] = len(record)

    #Diccionarios para el nombre, id y descripcion de cada record
    d['Names:'] = []
    d['IDs:'] = []
    d['Descriptions:'] = []

    #Asignacion de records
    for seq_record in SeqIO.parse(nombre_archivo,tipoArchivo):
        d['Names:'].append(seq_record.name)
        d['IDs:'].append(seq_record.id)
        d['Descriptions:'].append(seq_record.description)

    return d

#Llamada a la funcion
if __name__ == "__main__":
	resultados = summarize_contents(archivo)
	print(resultados)
