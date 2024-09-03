import hashlib
import SHA256

from Crypto.Hash import SHA256


def mine_block(previous_hash, transactions, difficulty):
    nonce = 0
    while True:
        block_contents = f"{previous_hash}{transactions}{nonce}".encode('UTF-8')
        block_hash = hashlib.sha256(block_contents).hexdigest()
        if block_hash.startswith('0' * difficulty):
            return nonce, block_hash
        nonce += 1

# Пример использования
previous_hash = '0000a1b2c3d4e5f6'
transactions = 'Alice pays Bob 50 BTC'
difficulty = 4  # количество нулей в начале хеша
nonce, block_hash = mine_block(previous_hash, transactions, difficulty)

print(f"Блок замайнен! Nonce: {nonce}, Хеш: {block_hash}")
