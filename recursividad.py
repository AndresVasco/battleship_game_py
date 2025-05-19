def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("ingrese el valor del que desea saber el factorial: "))
print(factorial(n))

#Sumatoria de Números naturales ejm: averiguar 4= 4+3+2+1

def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria (n-1)
    
n = int(input("Ingrese el valor del que desea conocer la sumatoria: "))
print("la sumatoria es: ",sumatoria(n))
