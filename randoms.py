import random

#Crear números enteros aleatorios
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleatorios
colors = ['Rojo', 'Azul', ' verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As', 'Rey', ' Reina','J','10']
random.shuffle(cards)
print(cards)