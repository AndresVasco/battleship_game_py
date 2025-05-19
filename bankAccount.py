class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("no se puede depositar, verifica con tu banco")
            
    def withdraw(self, amount):
        if self.active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. El saldo actual es {self.balance}")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada.")
    
    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada.")
        
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Andres", 1000)

#Llamada a los metodos
account1.deposit(2000)
account2.deposit(100)
account1.deactivate_account()
account1.activate_account()
account1.deposit(50)


# Para crear un objeto la nomenclatura es parecida a la variable donde decimos el nombre = asignacion
# luego el nombre de la clase seguida d elos parametros que necesitamos para construir el objeto
#NOMBRE = CLASE (PARAMETROS)

#EN PYTHON TODO ES UNA CLASE