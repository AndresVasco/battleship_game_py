import json

#Lectura del archivo JSON
with open('products.json', mode ='r' ) as file:
    products = json.load(file)
    
#Mostrar el contenido del archivo JSON
for product in products:
    #print(product)
    print(f"Prodcut: {product['name']}, Price:{product['price']}") #Podemos iterar para sacar elementos especificos del JSON