import json

file_path = 'products.json'

new_product = {
    "name": "Wireles Charger",
    "price": 91,
    "quantity": 100,
    "brand": "ChargerMaster",
    "category": "Accessories",
    "entry_date":"2025-05-08"
}

with open (file_path, mode='r') as file:
    products = json.load(file)
    
products.append(new_product)

with open (file_path, mode='w') as file:
    json.dump(products, file, indent=4)  #Especificamos el la informacion que queremos escribir en el JSon, luego el archivo y por ultimo la identacion que queremos
    #Se va a poder añadir tantos como queramos, solo es darle correr el programa y se va a añadir al JSON