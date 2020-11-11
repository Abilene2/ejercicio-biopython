Ejercicio Bioinformatica 

sript.py
Se creo el archivo llamado script.py que contiene las funciones:
    summarize_contents(), que recibe el nombre una archivo y genera un diccionario de python con en el nombre, la ruta, el numero de records y el nombre, id y descripcion de los records.

    concatenate_and_get_reverse_of_complement(), la cual a partir de dos cadenas crea dos obejtos Seq los concatena y devuelve el reverso complementario.

    print_proteins_and_codons_using_standard_table(), que recibe una cadena, la convierte en un objeto Seq y devuelve un diccionario con el mRNA que codifica, la secuecia de la proteina si hay un codon de inicio y el codon de termino si existe, la traduccion se hace usando la tabla estandar.

    print_proteins_and_codons_using_mitocondrial_yeast_table(), que recibe una cadena, la convierte en un objeto Seq y devuelve un diccionario con el mRNA que codifica, la secuecia de la proteina si hay un codon de inicio y el codon de termino si existe, la traduccion se hace usando la tabla con el codigo mitocondrial de la levadura.

test_script.py
El archivo test_script.py contiene a las funciones: 
    test_summarize_contents(), para revisar la funcion con tres archivos de tipo fasta y tres archivos de tipo genbank.

    test_concatenate_and_get_reverse_of_complement(), la cual contiene cinco pruebas con diferentes cadenas y no cadenas para la funcion.

    test_print_proteins_and_codons_using_standard_table(), con cinco pruebas para revisar que funcione en el caso de no mandar una cadena de longuitud multiplo de 3, y otros casos.

    test_print_proteins_and_codons_using_mitocondrial_yeast_table(), con cinco pruebas para revisar que funcione en el caso de no mandar una cadena de longuitud multiplo de 3, y otros casos.

/data
Contine archivos de tipo fasta y genbank para realizar las pruebas de summarize_contents.