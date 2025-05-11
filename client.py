import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5050))

client_socket.sendall(b'Hello Server!')

data = client_socket.recv(1024)
print("Response from server:", data.decode())

client_socket.close()
