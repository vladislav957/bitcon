import ssl
import socket

# Настройка SSL-контекста
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations('server.crt')

# Создание SSL-соединения
client_socket = socket.create_connection(('localhost', 8443))
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Отправка данных серверу
ssl_socket.send(b"Hello, SSL server!")

# Получение ответа от сервера
data = ssl_socket.recv(1024)
print(f"Received: {data.decode()}")

# Закрытие соединен
