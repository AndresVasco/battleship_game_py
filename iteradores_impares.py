#Crrear un iterador para los # impares

#Limite
limit   = 10

#Crear iterador
odd_iter = iter(range(1, limit+1,2)) #Si quiero obtener los # Pares solo es cambiar ese primer 1 por un 0

#Usar el iterador
for num in odd_iter:
    print(num)
    
    
    
#Crear un iterador para # pares

#limite
limit = 11

#Creando el iterador
pair_iter = iter(range(2, limit+1,2))

#usandso el iterador
for num in pair_iter:
    print(num)