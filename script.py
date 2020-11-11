from Bio import SeqIO, Seq
from Bio.Seq import Seq
import os

#archivo = os.path.abspath("AF323668.gbk")

#Definicion de la funcion summarize_contents()
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

#Definicion de la funcion concatenat_and_get_reverse_of_complement
def concatenate_and_get_reverse_of_complement(seq_1, seq_2):
    if (type(seq_1)==str) & (type(seq_2) == str):
        S1 = Seq(seq_1)
        S2 = Seq(seq_2)
        seq_conc = S1 + S2
        return seq_conc.reverse_complement()
    else:
        raise TypeError("No es una cadena")  

#Definicion de la funcion print_proteins_and_codons_using_standard_table
def print_proteins_and_codons_using_standard_table(seq):
    dna = Seq(seq)
    mRna = dna.transcribe()
     
    #Diccionario 
    d = {}
    d["mRNA"] = [mRna]
    d["protein"] = []
    d["stop_codon"] = []

    #Revisar si tiene codon de inicio
    codon_inicio = False
    for codon in range(0,len(dna),3):
        if "ATG" in dna[codon:codon+3]:
            #Variable con la posicion del primer aa del codon de inicio
            posicion_inicio = codon
            dnaCoding = dna[codon:len(dna)]
            
            d["protein"] = dnaCoding.translate(to_stop = True)
            #Si hay codon de inicio
            codon_inicio = True
            #Solo para encontrar un codon 
            break

        if "CTG" in dna[codon:codon+3]:
            #Variable con la posicion del primer aa del codon de inicio
            posicion_inicio = codon
            dnaCoding = dna[codon:len(dna)]
            
            d["protein"] = dnaCoding.translate(to_stop = True)
            #Si hay codon de inicio
            codon_inicio = True
            #Solo para encontrar un codon 
            break

        if "TTG" in dna[codon:codon+3]:
            #Variable con la posicion del primer aa del codon de inicio
            posicion_inicio = codon
            dnaCoding = dna[codon:len(dna)]
            
            d["protein"] = dnaCoding.translate(to_stop = True)
            #Si hay codon de inicio
            codon_inicio = True
            #Solo para encontrar un codon 
            break

    #Si si lo hay buscar codon de paro despues del codon de inicio  
    if codon_inicio == True:
        for codon in range(0,len(dna),3):
            #print(dna[codon:codon+3])
            if ("TAG" in dna[codon:codon+3]) & (posicion_inicio < codon):
                d["stop_codon"].append("TAG")
                break
            if ("TAA" in dna[codon:codon+3]) & (posicion_inicio < codon):
                d["stop_codon"].append("TAA")
                break
            if ("TGA" in dna[codon:codon+3]) & (posicion_inicio < codon):
                d["stop_codon"].append("TGA")
                break
                 
    return d

#Definicion de la funcion print_proteins_and_codons_using_standard_table
def print_proteins_and_codons_using_mitocondrial_yeast_table(seq):
    dna = Seq(seq)
    mRna = dna.transcribe()
     
    #Diccionario 
    d = {}
    d["mRNA"] = [mRna]
    d["protein"] = []
    d["stop_codon"] = []

    #Revisar si tiene codon de inicio
    codon_inicio = False
    for codon in range(0,len(dna),3):
        if "ATG" in dna[codon:codon+3]:
            #Variable con la posicion del primer aa del codon de inicio
            posicion_inicio = codon
            dnaCoding = dna[codon:len(dna)]
            
            d["protein"] = dnaCoding.translate(to_stop = True, table = 3)
            #Si hay codon de inicio
            codon_inicio = True
            #Solo para encontrar un codon 
            break

        if "ATA" in dna[codon:codon+3]:
            #Variable con la posicion del primer aa del codon de inicio
            posicion_inicio = codon
            dnaCoding = dna[codon:len(dna)]
            
            d["protein"] = dnaCoding.translate(to_stop = True, table = 3)
            #Si hay codon de inicio
            codon_inicio = True
            #Solo para encontrar un codon 
            break

        if "GTG" in dna[codon:codon+3]:
            #Variable con la posicion del primer aa del codon de inicio
            posicion_inicio = codon
            dnaCoding = dna[codon:len(dna)]
            
            d["protein"] = dnaCoding.translate(to_stop = True, table = 3)
            #Si hay codon de inicio
            codon_inicio = True
            #Solo para encontrar un codon 
            break

    #Si si lo hay buscar codon de paro despues del codon de inicio  
    if codon_inicio == True:
        for codon in range(0,len(dna),3):
            #print(dna[codon:codon+3])
            if ("TAG" in dna[codon:codon+3]) & (posicion_inicio < codon):
                d["stop_codon"].append("TAG")
                break
            if ("TAA" in dna[codon:codon+3]) & (posicion_inicio < codon):
                d["stop_codon"].append("TAA")
                break
                 
    return d