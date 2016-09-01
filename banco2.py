import threading
import time

class Cuenta:
	def __init__ (self,saldo):
		self.saldo=saldo

	def retirar(self,nombre,cantidad):
		if self.saldo>cantidad:
			time.sleep(0.2)
			print(nombre," hizo un retiro")
			self.saldo-=cantidad
			print("El saldo actual es de: ",self.saldo)

c=Cuenta(300)

hilos=[]

for i in range(1,100):
	hilos.append(threading.Thread(target=c.retirar,args=("Rogelio",30)))
	hilos.append(threading.Thread(target=c.retirar,args=("Valeria",50)))
	hilos.append(threading.Thread(target=c.retirar,args=("Daniel",90)))

for hilo in hilos:
	hilo.start()
	hilo.join()

print("El saldo final de la cuenta es: $",c.saldo)

