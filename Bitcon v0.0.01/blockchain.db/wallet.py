from mimetypes import init
from typing import Self
from webbrowser import get
import Blockchain.py
import hashlib
import SHA256

    
class TransactionSystem:
    def init(self,tansaction_type,amount):
        self.balance = 0
        self.tansaction_type = tansaction_type # 'in' ��� �����,'out' ��� ������
        self.amount = amount
        
        def str(self):
            print f"{self.tansaction_type} - {self.amount}"    
            
            def init(self):
                self.tansaction = []
                self.balance = 0
                
                def add_tansaction(delf,tansaction):
                    if tansaction.tansaction_type == 'in':
                    self.balance += tansaction.amount
                    self.tansaction.appenend(tansaction)
                    self.tansaction.tansaction_type == 'out'
                def balance -= tansaction.amount else:
    
    def calculeta_hash(data,previous_hash):
     new_varnew_var = hashlib.sha256
     sha256.update((str(date)) + str(previnun_hash)).encode('utf-8')
     peturn .sha256.hexdigest()
            
    print("����������� ��� ����������")
    print(f"��������� ���������:{tansaction}")
    
    def get_balance(self):
        return self.balance
    def get_tansaction_history(self):
        return self.tansaction
    
    # 4b8a4de720e81bde8c35cefa0cc61cbf82d3764bcdc2bcb53507a05a04660026
    tansaction_system = TransactionSystem()
    
    #49eb0704cbb78f608064ad23de097a334065e8760a6cadc343960f710b1af803
    tansaction_system.add_tansaction(Tansaction('in,100'))
    
    # ��������� ��������� ����������
    tansaction_system.add_tansaction(Tansaction('out',50))
    
    # �������� ������
    print(f"������� ������: {tansaction_system.get_balance()}")
    
    # ������� ������� ����������
    print("������� ����������:")
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
    
# C:\Users\LENOVO\Desktop\Bitcon\Bitcon.py\Blockchain.py CacheWallet
wallet = TransactionSystem()
wallet.get_balance()  # ����� �������)��� ������� (0,000000)
wallet.deposit(100)   # ������� 100 ������
wallet.get_balance()  # ����� ������� ����� �������� (100)
wallet.withdraw(50)   # ������ 50 ������
wallet.get_balance()  # ����� ������� ����� ������ (50)
wallet.withdraw(100)  # ������� ����� ������, ��� ���� �� ������� (��������� �� ������)
wallet.get_balance()  # ����� ������� ����� ��������� ������� ������ (50)