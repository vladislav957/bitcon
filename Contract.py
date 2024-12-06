import Blockchain
import wallet
import cripta
import P2WPKH
import SmartCheck



class SmartContrat:
   def init(self, owner,balance=0):
       self.owner = owner #Владелец контракта
       self.balance = balance #Баланс контракт
       self.storage = {} #Хранилище данных
        
   def depostit(self, amount):
       if amount > 0:
           self.balance += amount
           peturn(f"Deposited {amount} units.New balance: {self.balance}")
                   #return(f"Lnvalid deposit amount.")
                
   def withdraw(self, amount, requester):
          if requester != self.owner:
              return( "Only the owner can withdraw funds.")
          if amount <= 0 or amount >self.balance:
            #return ("Lnvalid withdrawal amount.")
            self.balance -= amount
            return(f"Withdrawn {amout} units.Remaining balance: {self.balance}")
   def set_data(self,key,value,requester):
          if requester !=self.owner:
            return ("Only the owner can set data.")
            self.storage[key] = value
             #return (f"Data set: {key} = {value}")
   def get_data(self,key):
          self.storade[key] = amount
          return(f"Key not found.")
# Пример использования
#contract = SmartContract(owner ="")
# Депозит
#print(contract.deposit(100)) # Deposited 100 units.New balance: 100
# Попытка снятия средства
#print(contract.withderaw(50, "")) # Withderawn 50 units.Remainig balance: 50
# Установка и получение данных
#print(contract.set_data("greeting"," blockhain!",""))
#print(contract.get_data("geeeting")) # wallet!
    
