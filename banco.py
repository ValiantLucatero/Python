import threading
import time

class Cuenta:
	def __init__ (self,saldo):
		self.saldo=saldo
		self.candado=threading.Lock()

	def retirar(self,cantidad):
		self.candado.acquire(4)
		if self.saldo-cantidad >=0:
			time.sleep(0.2)
			print("Se hizo un retiro")
			self.saldo-=cantidad
			print("El saldo actual es de: ",self.saldo)
		self.candado.release()

c=Cuenta(50)
h=[]

for i in range(10):
	h.append(threading.Thread(target=c.retirar,args=(10,)))

for hilo in h:
	hilo.start()
