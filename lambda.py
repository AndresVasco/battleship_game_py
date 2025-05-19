#Van a haber casos en los que vamos a querer hacer una op sencilla
#No se necesita crear funcion, se pueden usar operaciones anonimas como lambda (Solo necesita parametros y aplicacion)

add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,100))

#Cuando se trabjaan listas y quermeos aplicar una funcion a cda elemento s epuede usar map y lambda
#map() Aplica una función a cada elemento de un iterable.


#Cuadraro de cada Numero
numbers = range(0,11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadradors:", squared_numbers)

#Se puede seleccionar los elementos si cumplen una condicion con filter
# filter() Filtra cada elemento de un iterable travez de una función.

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers) 


