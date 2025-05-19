numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Andres",
               "Apellido": "Vasco",
               "Altura": 2.04,
               "Edad": 29}
print(information)
del information ["Edad"]
print(information)
claves = information.keys()  #Claves todo lo que se realice con los diccionario va a tener estas propiedades
print(claves)
print(type(claves))
values = information.values()  #Valores
print(values)
pairs = information.items()  #items - separa en tuplas la clave y el valor
print(pairs)
contacts = {"Andres": {"Apellido": "Vasco",
               "Altura": 2.04,
               "Edad": 29},
               "Ana": {"Apellido": "Arboleda",
               "Altura": 1.67,
               "Edad": 31}}
print(contacts["Ana"])