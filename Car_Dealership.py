#Se a a vender y comprar
#un user va a poder preguntar disponibilidad, precio y posibilidad de compra

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehiculo {self.model} ha sido vendido")
        else:
            print(f"El vehiculo {self.model} no está disponible")
    
    def buy(self):
        self.available = True
        print(f"El vehiculo {self.model} ha sido comprado")
        
class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.buyed_vehicles = []
    
    def buy_vehicle(self, vehicle):
        if vehicle.available:
            vehicle.sell()
            self.buyed_vehicles.append(vehicle)
        else: 
            print(f"El vehiculo {vehicle.model} no se encuentra disponible.")
    
    def sell_vehicle(self, vehicle):
        if vehicle in self.buyed_vehicles:
            vehicle.sell()
            self.buyed_vehicles.remove(vehicle)
        else:
            print(f"El vehiculo {vehicle.model} no está disponible en la lista")
            
class Inventory:
    def __init__(self):
        self.vehicles = []
        self.clients = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"El vehiculo {vehicle.model} ha sido agregado.")
        
    def register_client(self, client):
        self.clients.append(client)
        print(f"El cliente {client.name} ha sido registrado.")
    
    def show_available_vehicles(self):
        print(f"Los vehiculos disponibles son: ")
        for vehicle in self.vehicles:
            if vehicle.available:
                print(f"{vehicle.model} por {vehicle.price}")

#Creando los vehiculos
vehicle1 = Vehicle("Yamaha", "Fazer600 S2", "4900 USD")
vehicle2 = Vehicle("Kawasaki", "Versys 650 ABS", "6500 USD")
vehicle3 = Vehicle("Renault", "Stepway", "8900 USD")

#Crear client
client1 = Client("Andres", "001")

#Crear inventario
inventory = Inventory()
inventory.add_vehicle(vehicle1)
inventory.add_vehicle(vehicle2)
inventory.add_vehicle(vehicle3)

#Registrar cliente
inventory.register_client(client1)

#Para mostrar vehiculos
inventory.show_available_vehicles()

#Cliente compra un vehiculo
client1.buy_vehicle(vehicle2)

#mostrar vehiculos luego de compra
inventory.show_available_vehicles()

#Comprar vehiculo
client1.sell_vehicle(vehicle2)

#mostrar vehiculos luego de compra
inventory.show_available_vehicles()
