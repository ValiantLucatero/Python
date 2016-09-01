#Servidor Multi cliente

import socket
import threading
import time

class HiloDelCliente(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.cliente=sock
	def run(self):
		cadena=self.cliente.recv(1024).decode("utf-8")
		while cadena != "salir":
			self.cliente.send(("Visto...").encode("utf-8"))
			print("Mensaje Recibido: ",cadena,"desde: ",threading.current_thread())
			cadena=self.cliente.recv(1024).decode("utf-8")
		self.cliente.close()

class Servidor():
	def __init__(self,ip="localhost",puerto=9000):
		self.sock=None
		self.ip=ip
		self.puerto=puerto
		self.listaHilos=[]

	def start(self):
		self.sock=socket.socket()
		self.sock.bind((self.ip,self.puerto))
		self.sock.listen(10)

		while True:
			try:
				self.sock.settimeout(1)
				print("Esperando...")
				cliente=self.sock.accept()[0]
			except socket.timeout:
				print("Servidor ZZZZZ")
				time.sleep(2)
				continue
			cl=HiloDelCliente(cliente)
			print("Se conecto un cliente en: ",cl.getName())
			self.listaHilos.append(cl)
			cl.start()

			for hilo in self.listaHilos:
				if not hilo.isAlive():
					self.listaHilos.remove(hilo)
					hilo.join()
		self.sock.close()

ip=input("Ingresa la ip para iniciar el Servidor: ")
puerto=int(input("Ingresa el numero de puerto: "))
server=Servidor(ip,puerto)
server.start()