import csv

#Leer archivo csv y capturar los datos en un diccionario
"""with open('products.csv', mode= 'r') as file:
    csv_reader = csv.DictReader(file) #Abrir el archivo formato diccionario
    for row in csv_reader:
        print(row)"""
        

#Mostrar la informacion por columna
with open('products.csv', mode= 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Prodcuto: {row['name']}, Precio: {row['price']}")