#Sockets (Cliente)

import socket

HOST="localhost"
#127.0.0.1
PORT=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST, PORT))

s.sendall("Hola Mundo".encode())
datos=s.recv(1024).decode()

print("Recibido del servidor:",repr(datos))
