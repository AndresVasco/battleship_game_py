class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print (f"Hello, my name is {self.name} and I am {self.age} years old.")
    
class Student(Person):
    def __init__(self, name, age, student_id): #Debo pedir exactamente los mismo atribuytos que se piden en Person
        super().__init__(name, age) #Llamo al constructor de la clase padre
        self.student_id = student_id
        
    def greet(self):
        super().greet() #Llamo al método greet de la clase padre
        print(f"Hello, my student ID is {self.student_id}.") 
        
Student = Student("Ana", 20, "S12345")
Student.greet() #Llamo al método greet de la clase hija

#El uso de super() en Python está relacionado con la herencia de clases. 
# Permite llamar métodos o acceder a atributos de la **clase padre** desde una **clase hija**, 
# sin necesidad de referenciar explícitamente el nombre de la clase padre. 
# Es especialmente útil cuando se trabaja con herencia múltiple o se desea extender la funcionalidad de la clase base sin sobrescribir 
# completamente su comportamiento.


#Diferencia entre el atributo y el argumento del constructor

#Te habrás fijado que name y self.name parecen ser lo mismo, pues no, son diferentes aunque contengan el mismo valor.

#La sentencia self.name hace referencia al atributo del objeto, 
# mientras que name hace referencia al valor del argumento de __init__ cuando se crea una instancia.