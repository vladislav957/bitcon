import ssl
import socket

# Настройка SSL-контекста
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# Создание сокета и ожидание соединения
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 443))
server_socket.listen(5)

# Принятие соединения и настройка SSL
conn, addr = server_socket.accept()
ssl_conn = context.wrap_socket(conn, server_side=True)

# Прием данных от клиента
data = ssl_conn.recv(1024)
#print(f"Received: {data.decode()}")

# Ответ клиенту
ssl_conn.send(b"")

# Закрытие соединения
ssl_conn.close()
server_socket.close()
print(f'Received: # \n {data.decode()}')
