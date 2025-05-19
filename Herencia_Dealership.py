#las clases hijas vana heredar todos los parametros que ponemos en esta superclase o clase padre:
class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulación son variables de instancia que contienen los datos privados del objeto
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available= False
            print(f"El Vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El Vehiculo {self.brand}. No está disponible")
        
    #Abstracción  solo podmeos acceder a las variables mediante los metodos get o check
    def check_available(self):
        return self.is_available
    
    #Abstracción
    def get_price(self):  #Cuando queremos devolver el valor de un parametro usamos el get 
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")   #Levantar una excepción
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase") 
    
#Herencia 
class Car(Vehicle):  #Para heredar los parametros de la super clase, cuando se cree una instancia tambien se debe pasar info que se vea en la clase padre
        #Polimorfismo hace referencia a que podemos tener muchas formas pero un comportamiento diferente 
        def start_engine(self):
            if not self.is_available:
                return f"El motor del vehiculo {self.brand} está en marcha"
            else:
                return f"El vehiculo {self.brand} no está disponible"
        
        #polimorfismo
        def stop_engine(self):
            if self.is_available:
                return f"El vehiculo {self.brand} se ha detenido"
            else:
                return f"El Vehiculo {self.brand} No está disponible"
            
#Herencia
class Bike (Vehicle):
    #polimorfismo hace referencia a que podemos tener muchas formas pero un comportamiento diferente 
    def start_engine(self):
            if not self.is_available:
                return f"La bicicleta {self.brand} está en marcha"
            else:
                return f"La bicicleta  {self.brand} no está disponible"
        
    #polimorfismo 
    def stop_engine(self):
            if self.is_available:
                return f"La bicicleta  {self.brand} se ha detenido"
            else:
                return f"La bicicleta  {self.brand} No está disponible"
            
class Truck (Vehicle):
    def start_engine(self):
            if not self.is_available:
                return f"El motor del camion {self.brand} está en marcha"
            else:
                return f"El camion  {self.brand} no está disponible"
        
    def stop_engine(self):
            if self.is_available:
                return f"El motor del camion  {self.brand} se ha detenido"
            else:
                return f"El camion  {self.brand} No está disponible"
            
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
        
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible.")
            
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No Disponible"
        print(f"El {vehicle.brand} está {availability} y tiene un precio de {vehicle.get_price()}")
        
        
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")
        
    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido a la lista")
        
    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"El vehiculo {vehicle.brand} por {vehicle.get_price()}")
                
                
car1 = Car("Ford", "Raptor", 20000)
bike1 = Bike("Kawasaki", "Versys 650", 8000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Andres")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consulta un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Encapsulamiento:* Agrupa datos y métodos relacionados en una clase. Oculta los detalles internos y controla el acceso a los datos.
#Ejemplo: Una clase "Coche" que encapsula propiedades como "color" y métodos como "arrancar".

#Abstracción:* Simplifica sistemas complejos ocultando detalles innecesarios. Permite centrarse en las características esenciales de un objeto.
#Ejemplo: Una interfaz "Vehículo" con método "mover", sin especificar cómo se implementa.

#Herencia:* Permite que una clase (hija) herede propiedades y métodos de otra (padre). Promueve la reutilización de código y la jerarquía de clases.
#Ejemplo: "Coche" y "Moto" heredan de "Vehículo".

#Polimorfismo:* Permite que objetos de diferentes clases respondan al mismo método de manera única. Facilita el uso de una interfaz común para tipos de datos diversos.
#Ejemplo: Diferentes tipos de "Vehículo" implementan el método "mover" de forma distinta.