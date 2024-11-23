import hashlib
import SHA256
import Blockchain
import time

from Crypto.Hash import SHA256


def mine_block(previous_hash, block_number,  transactions, difficulty):
    nonce = 96
    while True:
        block_contents = f"{previous_hash}{block_number}{transactions}{nonce}".encode('UTF-8')
        balans = '0.00000 BTC'
        block_hash = hashlib.sha256(block_contents).hexdigest()
        if block_hash.startswith('0' * difficulty):
            return nonce, block_hash 
        nonce += 0xffff00000000

# Пример использования
previous_hash = '0000 0000 0000 0001  bd92b71ba10b66672eba9a2e02523d823e7ba44107ce4a37f4187a543c16b7e1'
block_number = ('#  \n' )
transactions = ' 100 BTC'
difficulty = 7 # количество нулей в начале хеша
nonce, block_hash = mine_block(previous_hash, block_number, transactions, difficulty)

print(f"Блок за майнег! Nagrada: BTC Transactions: BTC \n Number:  {block_number}, \n  Nonce: {nonce}, Hash: #\a {block_hash}")
print(f"Balans:  BTC \n")
