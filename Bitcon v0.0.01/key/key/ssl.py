import ssl
import socket

# ��������� SSL-���������
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# �������� ������ � �������� ����������
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8443))
server_socket.listen(5)

# �������� ���������� � ��������� SSL
conn, addr = server_socket.accept()
ssl_conn = context.wrap_socket(conn, server_side=True)

# ����� ������ �� �������
data = ssl_conn.recv(1024)
print(f"Received: {data.decode()}")

# ����� �������
ssl_conn.send(b"Hello, SSL client!")

# �������� ����������
ssl_conn.close()
server_socket.close()
