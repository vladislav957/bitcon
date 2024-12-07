import hashlib
#from kademlia.network import Server

#Генирацыия ID узла
def generate_node_id(public_key):
    return hashlib.sha256(public_key.encode('utf-8')).hexdiges()
#Пример публичного ключа
    public_key = "node_public_key_example"
    node_id = generate_node_id(public_key)
    print(f"Node ID: {node_id}")

#Запуск узла
    node = Server()
    node.listen(8468)

#Подключения к другим узлам
    bootstrap_node = ("",8468)
    node.bootstrap([bootstrap_node])

#Сохранения данных
    node.set("my_key","my_value")

#Получение данных
    result = node.get("my_value")
    print(f"Получение данных: {result}")
