#Cuando se están creando funciones debemos asegurarnos de llamarlas al final:

def greet(name, last_name):
    print("Hola", name, last_name)
    
greet("Andres", "Vasco")
greet("Ana", "Arboleda") 

# Hay casos donde no se da la información explicita sino que se tiene un valor predeterminado:

def greet(name, last_name = "No tiene apellido"): #esto sugiere que cuando no se cumpla la variable, se manda ese valor por defecto
    print("Hola", name, last_name)
    
greet("Andres", "Vasco")
greet("Ana") 

# Tambien podemos mandar parametros posicionales (de manera desordenada) soilo haciendo referencia al parametro:

def greet(name, last_name):
    print("Hola", name, last_name)
    
greet("Andres", "Vasco")
greet(last_name="Arboleda", name="Ana") 