Ejercicio Bioinformatica 

sript.py \n
Se creo el archivo llamado script.py que contiene las funciones:
    summarize_contents()
Recibe el nombre una archivo y genera un diccionario de python con en el nombre, la ruta, el numero de records y el nombre, id y descripcion de los records.

    concatenate_and_get_reverse_of_complement()
La cual a partir de dos cadenas crea dos obejtos Seq los concatena y devuelve el reverso complementario.

    print_proteins_and_codons_using_standard_table()
Recibe una cadena, la convierte en un objeto Seq y devuelve un diccionario con el mRNA que codifica, la secuecia de la proteina si hay un codon de inicio y el codon de termino si existe, la traduccion se hace usando la tabla estandar.

    print_proteins_and_codons_using_mitocondrial_yeast_table()
Recibe una cadena, la convierte en un objeto Seq y devuelve un diccionario con el mRNA que codifica, la secuecia de la proteina si hay un codon de inicio y el codon de termino si existe, la traduccion se hace usando la tabla con el codigo mitocondrial de la levadura.

test_script.py \n
El archivo test_script.py contiene a las funciones: 
    test_summarize_contents()
Revisar la funcion summarize_contents con tres archivos de tipo fasta y tres archivos de tipo genbank.

    test_concatenate_and_get_reverse_of_complement()
Contiene cinco pruebas con diferentes cadenas y no cadenas para la funcion concatenate_and_get_reverse_of_complement.

    test_print_proteins_and_codons_using_standard_table()
Contienecinco pruebas para revisar que funcione en el caso de no mandar una cadena de longuitud multiplo de 3, y otros casos.

    test_print_proteins_and_codons_using_mitocondrial_yeast_table()
Contiene cinco pruebas para revisar que funcione en el caso de no mandar una cadena de longuitud multiplo de 3, y otros casos.

/data
Contine archivos de tipo fasta y genbank para realizar las pruebas de summarize_contents.