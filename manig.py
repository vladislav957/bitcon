from concurrent.futures import ThreadPoolExecutor 
import hashlib
import SHA512
import Blockchain
import time
import P2P
import IP

from Crypto.Hash import SHA512


def mine_block(previous_hash, block_number, Blockchain, transactions, difficulty):
    nonce = 96
    
    while True:
        block_contents = f"{previous_hash}{block_number}{Blockchain}{transactions}{nonce}".encode('UTF-8')
        Balances = 0.00000 
        block_hash = hashlib.sha512(block_contents).hexdigest()
        if block_hash.startswith('0' * difficulty):
            return nonce, block_hash 
        nonce += 0xffff00000000
        
def Blockchain(block_number, P2P, time):
    blocl_number = 31.000000
    
    while True:
        block_contents = f"{previous_hash}{block_number}{P2P}{time}".ecode('UTF-8')
        block_number = P2P.time(block_contents).hexdigest()
        if block_number.startswith('0' * time):
           return number, P2P
        block_number += 0xffff000000
        
def apply_camera(char, camera):
    return(char['x']-camera['x'], char['y']-camera['y'])
def distance(p1, p2):
    distX = p1['x'] - p2['x']
    distY = p1['y'] - p2['y']
    dist = ((distX**2) + (distY**2)) ** (1/2)
    if dist <= (p1['r'] + p2['r']):
        return True
    return False
        
def Transactions(self,index,previus_hash,data,public_key,blockchain):
    transactions_block = 0xfff

    
    while True:
        self.index = index 
        self.previous_hash = previus_hash
        self.data = data
        self.public_key = public_key
        self.hash = self.calclate_hash()
        self.blockchain.db = blockchain.db
        return public_key,data,blockchain
        transactions_block += 0xffff0000000

def  static_PyObject(self,static,PyOject):

    while True:
     #static pyObject *
     spam_system(PyObject *self, PyObject *args)
     {
     #const char *command;
     #int sts;

     #if (!PyArg_ParseTuple(args, "s", &command))
     #return NULL;
     self := PySpam_System(command)
      #return PyLong_FromLong(self);
     }
     

# Пример использования
previous_hash = ' '
block_number =  sum 
transactions =  0xff 
difficulty = 7 # количество нулей в начале хеша
nonce, block_hash = mine_block(previous_hash, block_number, Blockchain, transactions, difficulty)

print(f"Блок за майнег! Nagrada: 50.000000 BDR  Transactions: 50.000000 BDR \n Number: # \a {block_number},   Nonce:  #\n {nonce} H/s, Hash: #\a {block_hash}")
print(f"Balances: 50.000000 BDR \n" )

