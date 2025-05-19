#Programación Orientada a Objetos POO
class Person: 
    def __init__(self, name, age): #El constructor es una fn propia y especial de las clases, aqui se definen atributos principales
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")
        
person1 = Person("Ana", 32)
person2 = Person("Andres", 26)

person1.greet()
person2.greet()

# A las funciones propias de una clase  o de un objeto se llama metodo

