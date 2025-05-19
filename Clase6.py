#Operadores Numéricos
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print("Parte entera de la División:", a // b)
print("Módulo:", a % b)
a += 2 #Se puede hacer operaciones solo con darle este significado a la variable - / *
print(a)

#REGLA PEMDAS
# Potenciacion      División
# Exponenciación    Adición
# Multiplicación    Sustracción

operation_1 = 2 + 3 * 4 #Si no ponemos el () esto va implicito Pirmero iria * y luego + 
operation_2 = (2 + 3) * 4 #Aqui estamos diciendole que inicie con la suma, lo cual afectaria el resultado
print(operation_1)
print(operation_2)
Operation_3 = (2+3) * (4**2) / 8 - 1 #Aplica PEMDAS pero primero saca el resultado de los aprentesis para seguir
print(Operation_3)