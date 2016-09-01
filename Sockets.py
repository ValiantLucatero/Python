#Sockets (Servidor)

import socket

HOST="localhost"
#127.0.0.1
PORT=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

conn,addr=s.accept()
print("Conectado con ",addr)

while True:
	datos=conn.recv(1024).decode()
	if not datos:
		break
	conn.sendall(datos.encode())

print("datos recibidos: ",datos)
conn.close()
