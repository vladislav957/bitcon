from Crypto.Hash import SHA256
import hashlib
import time
import random
import Blockchain
import datetime as data


# Комбинируем текущий момнт времени и случайное значение
input_data = str(time.time()) + str(random.randint(0, 31000000))

# Xешируем комбинировованные данные
result = hashlib.sha256(input_data.encode('UTF-8')).hexdigest()
previous_hash = '000.000.000.001'

# Пример строки
data ='{[]}'

# Создаем объект хеширования и обновляем его данными
sha256_hash = SHA256.new(data.encode('utf-8'))

# Получаем хеш в виде шестнадцатеричной строки
hash_hex = sha256_hash.hexdigest()
print(f"Bitcon Block: #\b # has been added to the blockhain!")
print(f"Hash:  \a",result)  
print(f"Miner: ? \n")


