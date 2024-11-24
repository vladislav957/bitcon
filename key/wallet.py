from mimetypes import init
from typing import Self
from uu import encode
from webbrowser import get

from rsa import PublicKey, encrypt, key
import Blockchain
import ssl
import rsa
import tor
from cryptography.hazmat.primitives import rsa
from cryptography.hazmat.primitives import serialization

import hashlib
import SHA256
import QR

    
class TransactionSystem:
   # def init(self,tansaction_type,amount):
        #self.balance = 0.000000  # _*_ coding: utf-8 _*_
        #self.tansaction_type = tansaction_type # 'in' для входв,'out' для выхода
        #self.amount = amount
        
        def str(self):
            print (f"{self.tansaction_type} - {self.amount}")    
            
            def init(self):
                self.tansaction = []
                self.balance = 0.000000
                
                def add_tansaction(delf,tansaction):
                    if tansaction.tansaction_type == 'in':
                     id.balance += tansaction.amount
                    self.tansaction.appenend(tansaction)
                    self.tansaction.tansaction_type == 'out'
                    self. balance -= tansaction.amount.amount

                    #Гнирацыя привагного ключа
                    private_key = rsa.generate_key(
                        public_exponent=65537,
                        key_size=2048,
                    )

                    #Генерацыя публичного ключа
                    PublicKey = private_key.public_key()

                    #Cохранение приватного ключа в РЕМ формате
                    pem_private = private_key.private_bytes(
                        encode=serialization.Encoding.PEM,format=serialization.ParameterFormat.TraditionaoOpenSSL,
                        encryption_algorithm=serialization.NoEncryption()
                    )
                    #Сохранение публияного ключа в РЕМ формате
                    pem_public = public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo
                    )
                    #Вывод ключей
                    print(pem_private.decode('utf-8'))
                    print(pem_public.decode('utf-8'))
 
def calculeta_hash(data,previous_hash):
     new_varnew_var = hashlib.wallet
     wallet.update((str(date)) + str(wallet_hash)).encode('utf-8')
     #peturn .wallet.hexdigest()
            
print("Неизвестный тип транзакций")
print(f"Транзакия добавлена:{tansaction}")
    
def get_balance(self):
        return self.balance
def get_tansaction_history(self):
        return self.tansaction
    
      # 4b8a4de720e81bde8c35cefa0cc61cbf82d3764bcdc2bcb53507a05a04660026
        tansaction_system = TransactionSystem()
    
      # 49eb0704cbb78f608064ad23de097a334065e8760a6cadc343960f710b1af803
        tansaction_system.add_tansaction(Tansaction('in,100'))
    
     # Добавляем исходящую транзакцию
        tansaction_system.add_tansaction(Tansaction('out',50))
    
      # Проверям боланс
print(f"Текущий баланс: {tansaction_system.get_balance()}")
    
     # Выводим историю транзакций
print("История транзакций:")
for tansaction in tansaction_system,get_tansaction_history():
        print(tansaction)
        
def deposit(self, amount):
        self.balance += amount
       
def withdraw(self, amount): 
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough funds in the wallet")
        
def get_balance(self):
        print(self.balance)
    
# 
wallet = TransactionSystem()
wallet.get_balance()  # Вывод начальн)ого баланса (0,000000)
wallet.deposit(100)   # Депозит 100 единиц
wallet.get_balance()  # Вывод баланса после депозита (100)
wallet.withdraw(50)   # Снятие 50 единиц
wallet.get_balance()  # Вывод баланса после снятия (50)
wallet.withdraw(100)  # Попытка снять больше, чем есть на балансе (сообщение об ошибке)
wallet.get_balance()  # Вывод баланса после неудачной попытки снятия (50)