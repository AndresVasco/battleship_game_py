# Tratamientos de posibles errores que pueden ser generados por codigo o por usuario
#se trata de dar una solucion o mensaje de que esta sucediendo usando el try except


try: 
    divisor = int(input("ingresa un número divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:   #Cada try va a tener almenos 1 except es buena practica poner el nombre de cada excepción
    print("La kgaste prro: El divisor no puede ser cero ponte pilas")
    print("Motivo de la Kgada: ", e)
except ValueError as e:  #Se puede capturar el error y hacerlo mas notorio agregando la e
    print("Amiguito, como vas a dividir un número con algo que no sea un número? Tas pendejo o que?")
    print("Motivo de la Kgada: ", e)
    
#IMPORTANTE:
#Las excepciones tienen jerarquia vamos a tener clases padre y clases hijos
#Se pueden tratar clases padres o clases hijo o clases padre donde se traten todas las clases de esa familia:

#def print_exception_hierarchy(exception_class, indent=0):
    #print(' ' * indent + exception_class.__name__)
    #for subclass in exception_class.__subclasses__():
        #print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
#print_exception_hierarchy(Exception)