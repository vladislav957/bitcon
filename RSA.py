from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
import wallet
import Blockchain
import socket


# Генерация пары ключей RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Сообщение, которое мы хотим подписать
message = b''

# Создание хеша SHA-256
digest = hashes.Hash(hashes.SHA256(), backend=default_backend()).encode('UTF-8')
digest.update(message)
hash_value = digest.finalize()

# Подпись хеша с использованием приватного ключа
signature = private_key.sign(
    hash_value,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(f"Подпись: {signature.hex()}")

# Проверка подписи с использованием открытого ключа
try:
    public_key.verify(
        signature,
        hash_value,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Подпись действительна!")
except Exception as e:
    print("Подпись недействительна:", e)




