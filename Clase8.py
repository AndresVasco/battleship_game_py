#Listas

to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"] #Esta e suna clase list
print(type(numbers))
mix = ["Uno", 2, 3.14, True, [1,2,3]] #Se alamcena cualquier tipo de datos
print(mix)
print(len(mix)) #Se puede averiguar cuantos elementos tiene
print("Primer elemento", mix[0]) #se puede buscar posiciones especificas
print("Segundo elemento", mix[1]) 
print("Ultimo elemento elemento", mix[-1]) 
string = "Hola mundo" #Tambien se pueden ver elementos especificos de una cadena (Slicing)
print("Primer elemento", string[0]) 
print("Segundo elemento", string[1]) 
print("Ultimo elemento elemento", string[-1]) 
print(mix[2:-2])

#METODOS

#Aumentar o añadir un nuevo valor al final de la lista (es un elemto independiente de la lista)
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)

#Cuando queremos añadir a una posicion en especifico
mix.insert(1,["a","b"])
print(mix)

#Consultar posicion o primera aparición de un elemento
print(mix.index(["a","b"]))

#Consultar cual es el elemento mayor y cual es el elemento menor
numbers = [1,2,100.01,90.45,3,4,5] 
print(numbers)
print("Mayor:", max(numbers))
print("Menor:", min(numbers))

#puedo eliminar elementos de la lista incluso la lista entera
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
print(numbers) #aparece el name error porque en ese momento del cod ya no existe la lista