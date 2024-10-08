import ssl
import socket

# ��������� SSL-���������
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations('server.crt')

# �������� SSL-����������
client_socket = socket.create_connection(('localhost', 8443))
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# �������� ������ �������
ssl_socket.send(b"Hello, SSL server!")

# ��������� ������ �� �������
data = ssl_socket.recv(1024)
print(f"Received: {data.decode()}")

# �������� ��������
