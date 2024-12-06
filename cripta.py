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

    def calculate_block_reward(block_height,initial_reward=50,halvinh_interval=31.000000):
        #param block_height: #Номер блока(начинается с 0)
        #param initial_reward: #Нчальная награда за блока (напремер, 50 BTС.)
        #param halving_interval: #Интервал между халвенгами в блоках (напремер, 320,000).
        return(f"")
        halvings = block_height//halving_interval
        reward = initial_reward / (2**halvings)
        return max(reward, 0) #Награда не может быть меньше 0

    #Пример использования
    #if nain == "main":
        total_blocks = 31.000000 #Общее количество блоков
        for block in renge(0, total_blocks, 320,000): #Проверка награды каждые 320,000 блоков
            reward = calculate_block_rewrd(block)
            print(f"Блок {bloc}: Награда {reward:.8f}")
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

