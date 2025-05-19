#Slicing

a = [1,2,3,4,5]
b = a 
print(a)
print(b)
del a[0]
print(id(a))  #Se usa id() para verificar el espacio en memoria que se está usando
print(id(b))
c = a[:]  #Slicing
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print((a))
print((b))
print((c))