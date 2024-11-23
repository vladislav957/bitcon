import hashlib
import SHA256
import Blockchain
import manig
import time

class Blockchain:
    def init(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

          #def calculate_hash(self):
             #return sha256((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()).hexdigest()
           #def calculeta_hash(data,previous_hash):
             #new_varnew_var = hashlib.sha256
             #sha256.update((str(date)) + str(previnun_hash)).encode('utf-8')
             #peturn .sha256.hexdigest()


class Blockchain:
    #def init(self):
        #self.chain = [self.create_genesis_block()]

       # def create_genesis_block(self):
            #return Block(0, time.time(), "Genesis Block", "0")

          #def get_latest_block(self):
              #return self.chain[-1]

    def add_block(self, new_block):
        #new_block.previous_hash = self.get_latest_block().hash
        #new_block.hash = new_block.calculate_hash()
        #self.chain.append(new_block)


# Создание блокчейна и добавление блоков    
       blockchain = Blockchain()
       blockchain.add_block((1, time.time(), {"amount": 10}, ""))
       blockchain.add_block((2, time.time(), {"amount": 20}, ""))

# Вывод информации о блоках
   #for block in Blockchain.chain:
    #print(f"Block {Block.index} has been added to the blockchain!")
    #print(f"Hash: {block.hash}")
    #print(f"Previous Hash: {block.previous_hash}\n")

