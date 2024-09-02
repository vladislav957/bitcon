from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Пример строки
data = b""   

# Создаем объект хеширования
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

# Обновляем объект хеша данными
digest.update(data)

# Получаем хеш
hash_bytes = digest.finalize()

# Преобразуем байты в шестнадцатеричную строку
hash_hex = hash_bytes.hex()

print(f"SHA-256: {hash_hex}")
