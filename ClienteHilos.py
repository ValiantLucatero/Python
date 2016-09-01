import socket
s=socket.socket()
host=input("Ingresa la ip: ")
puerto=int(input("Ingresa el puerto: "))
s.connect((host,puerto))

while True:
	cadena=input("Mensaje: ")
	s.send(cadena.encode("utf-8"))
	recibido=s.recv(1024).decode("utf-8")
	print(recibido)
	if cadena=="salir":
		break

s.close()