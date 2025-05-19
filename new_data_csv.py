import csv

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'catehory': 'Accessories',
    'entry_date': '2025-05-05',
}

with open ('products.csv', mode = 'a', newline = '') as file:
    file.write('\n')
    csv_writer = csv. DictWriter(file,  fieldnames= new_product.keys()) #extraer claves del diccionario
    csv_writer.writerow(new_product) #decirle que se va a escribir una fila