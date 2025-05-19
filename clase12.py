#Uso del For para iterar entre datos

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:", i+1)
    
bikes = ["R1", "R8", "FZ6", "Versys 650"]
for name in bikes:
    print("Este es el nombre:", name)

#Usando el range, va desde el cero hasta un # antes del # que le estamos pidiendo, tambien s epuede usar el if

for i in range(3, 10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")
        
        
#Usando While para iterar, se debe tomar en cuenta que se debe modificar la condicional para que se detenga el
#codigo, d elo contrario se vuelve un bucle infinito (se interrumpe el bucle con CTRL + C en la terminal)
x = 0
while x<5:
    if x ==3:
        break #Para buscar evaluar un dato en especifico dentro del while se usa break, cuando se llega al valor
            #el while se termina
    print(x) 
    x+=1   #agregando esto se va a sumar un número a la busqueda hasta cumplir el requisito, asi se evita el bucle
    
    
#Para saltar u omitir el paso que estoy evaluando sin terminar el codigo se usa continue
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        continue
    print("Aquí i es igual a:", i)