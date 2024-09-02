from unittest import result
from Crypto.Hash import SHA256
import hashlib
import time
import random


# Комбинируем текущий момнт времени и случайное значение
input_data = str(time.time()) + str(random.randint(0, 1000000))

# Xешируем комбинировованные данные
result = hashlib.sha256(input_data.encode()).hexdigest()

print("SHA-256:", result)

# Пример строки
data ="№ Пример строки для хеширования"

# Создаем объект хеширования и обновляем его данными
sha256_hash = SHA256.new(data.encode('utf-8'))

# Получаем хеш в виде шестнадцатеричной строки
hash_hex = sha256_hash.hexdigest()

print(f"SHA-256: {hash_hex}")
