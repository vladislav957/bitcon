from unittest import result
from Crypto.Hash import SHA256
import hashlib
import time
import random
import Blockchain
import datetime as data


# Комбинируем текущий момнт времени и случайное значение
input_data = str(time.time()) + str(random.randint(0, 31000000))

# Xешируем комбинировованные данные
result = hashlib.sha256(input_data.encode()).hexdigest()
previous_hash = '000.000.000.001'

# Пример строки
data ='{[]}'

# Создаем объект хеширования и обновляем его данными
sha256_hash = SHA256.new(data.encode('utf-8'))

# Получаем хеш в виде шестнадцатеричной строки
hash_hex = sha256_hash.hexdigest()
print(f"Bitcon Block: #\b # has been added to the blockhain!")
print(f"Hash: 0000 0000 0000 0001 \a",result)  
print(f"Performane:  % \n")
print(f"Distance: h:m:s \n")
print(f"Transactions: #\n")
print(f"Depth: #\n")
print(f"Version: 0x300000 \n")
print(f"Merkle root:   387475d3b93525a16f748e1061f453c99f14a244126bdf10f8ae3e0fa7911860 \n")
print(f"Nonce: #\n")
print(f"Miner: ? \n")


