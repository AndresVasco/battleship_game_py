#Leer un archivo de texto linea por linea

"""with open("Cuento.txt", "r") as file: # abrir el archivo en modo lectura
    for lineas in file:
        print(lineas.strip())# remover los saltos de linea""" 
        
#Leer las lineas de un archivo y guardarlas en una lista

"""with open("Cuento.txt", "r") as file: # abrir el archivo en modo lectura
    lines = file.readlines() # leer todas las lineas y guardarlas en una lista
    print(lines) # imprimir la lista de lineas"""
    

#Escribir algo en un archivo de texto
""" with open("Cuento.txt", "a") as file: # abrir el archivo en modo escritura (append)("a")
    file.write("\n \nBy:ChatGPT") # agregar un texto al final del archivo" """
    
#sobreescribir un archivo de texto
""" with open("Cuento.txt", "w") as file:
    file.write("\n \nBy:ChatGPT") # sobreescribir el archivo con un texto nuevo """
    
#Contar el numero de lineas de un archivo de texto
with open("Cuento.txt", "r") as file:
    lineas = file.readlines() # leer todas las lineas y guardarlas en una lista
    print("El npumero de lineas es: ",len(lineas)) # contar el numero de lineas y guardarlas en una variable  