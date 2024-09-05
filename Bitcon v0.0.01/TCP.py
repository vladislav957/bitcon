import socket
import json


def start_server(host='127.0.0.1', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключился узел {addr}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено: {data}")
        client_socket.close()
        
def connect_to_server(host='127.0.0.1', port=5000, message="Привет"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(message.encode('utf-8'))
    client_socket.close()
    
data = {"block": "block_data"}
json_data = json.dumps(data)
    