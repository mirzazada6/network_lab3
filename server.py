import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5050))
server_socket.listen(1)
print("Server is listening on 127.0.0.1:5050...")
conn, addr = server_socket.accept()
print(f"Connection accepted from {addr}")
data = conn.recv(1024)
print("Received from client:", data.decode())
response = "Received your message"
conn.sendall(response.encode())
conn.close()
server_socket.close()
print("Connection closed.")
