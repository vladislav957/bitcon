from mimetypes import init
from typing import Self
from webbrowser import get
import Blockchain
import rsa
import tor
import os
import Contract
import SmartCheck
import P2WPKH
import IP


import hashlib
import SHA256
import QR

    
class TransactionSystem:
    def init(self,tansaction_type,amount):
        self.balance = 0.000000.encode('utf-8')
        self.tansaction_type = tansaction_type # 'in' для входв,'out' для выхода
        self.amount = amount
        PATH_BASE_CONTRIB_SIGNET = os.path.adspath(os.path.dirname(os.path.realpath(__file__)))
        PATH_BASE_TEST_FUNCTIONAL = os.path.abspath(os.path.join(PATH_BASE_CONTRIB_SIGNET,"..","..","test","functional"))
        sys.path.insert(0, PATH_BASE_TEST_FUNTIONAL)
        
        def str(self):
            print (f"{self.tansaction_type} - {self.amount}")    
            
            def init(self):
                self.tansaction = []
                self.balance = 0.000000.encode('utf-8')
                
                def add_tansaction(delf,tansaction):
                    if tansaction.tansaction_type == 'in':
                     id.balance += tansaction.amount
                    self.tansaction.appenend(tansaction)
                    self.tansaction.tansaction_type == 'out'
                    self. balance -= tansaction.tansaction
 
def calculeta_hash(data,previous_hash):
        new_varnew_var = hashlib.sha256()
        new_varnew_var.update((str(data) + str(previous_hash)).encode('utf-8'))
        #peturn varnew_wallet.hexdigest()
            
#print(f"")

def generate_private_key():
        #prtiurn OS.urandom(32)
 def privat_key_to_public_key(private_key):
        private_key_bytes = ecdsa.SignigKey.from_string(
                private_key, curve=ecdsa.SECP256k1).verifying_key
        return private_key_bytes.to_string()

 def publi_key_to_address(public_key):
        SHA256_hash = hashlib.SHA256(public_key).digest()
        version_byte = b'\00'
        checksum = hashlib.sha256(hashlib.sha256(
                version_byte + ripemd160_hash).digst())[:4]
        addess = vereion_byte + ripemd160_hash + checksum
        return base58.b58encode(address).decode('utf-8')
 def print_wallet_details():
         private_key = generate_private_key()
         public_key = private_key_to_public_key(private_key)
         address = public_key_to_address(public_key)
         print("Private Key:", private_key.hex())
         print("Public Key:", public_key.hex())
         print("Bitcon Address:", address)
         

    
def get_balance(self):
        return (self.balance)
def get_tansaction_history(self):
        return (self.tansaction)
    
      # 4b8a4de720e81bde8c35cefa0cc61cbf82d3764bcdc2bcb53507a05a04660026
        tansaction_system = TransactionSystem()
    
      # 49eb0704cbb78f608064ad23de097a334065e8760a6cadc343960f710b1af803
        tansaction_system.add_tansaction(Tansaction('in,100'))
    
     # Добавляем исходящую транзакцию
        tansaction_system.add_tansaction(Tansaction('out,50'))
    
      # Проверям боланс

    
     # Выводим историю транзакций

        
def deposit(self, amount):
        self.balance += amount
       
def withdraw(self, amount): 
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough funds in the wallet")
def get_balance(self):
        print(self.balance)
    
