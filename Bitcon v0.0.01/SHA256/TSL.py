import ssl

#Create an SSL context
context =
ssl.create_default_context()

#Make a connection_using the SSL context
with socket.crate_connectio n(("https://bitcoincore.org/",443)) as sock:
    with context.wrap_socket(sock,server_hostname="https://bitcoincore.org/")as ssock:

ssock.sendall(b"GET/HTTP/1.1\r\nHost: https://bitcoincore.org\r\n\r\n")
response = ssock.recv(1024)
print(response)

