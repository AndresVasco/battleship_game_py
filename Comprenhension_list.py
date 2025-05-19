# List comprenhensions: [Expresion for item in iterable if condition] se pueden construir listras de manera conciza
# Y eficiente

squares = [x**2 for x in range(1,11)] # el ** Significa elevado a la n potencia, el for aplica la primera condicion a todos los elementos
# print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
#print("Temperatura en F:", fahrenheit)

#Hallar Numeros pares
evens = [x for x in range(1,21) if x%2 ==0 ] #Tambien se puede usar el ifs
# print(evens)

#Hallar la transpuesta de una Matriz
#puede ser que nos lleve varias lienas de codigo hacer estr tipo de modificaciones con matrices
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)