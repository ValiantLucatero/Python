#Hilos

import threading

def saluda(nombre):
	print("Hola ",nombre)

hilo1=threading.Thread(target=saluda,args=("Juan",))
hilo2=threading.Thread(target=saluda,args=("Rogelio",))

hilo1.start()
hilo2.start()

x=0
class Resta(threading.Thread):
	def run(self):
		global x
		while x>-50:
			x-=1
			print("-:",x)

class Suma(threading.Thread):
	def run(self):
		global x
		while x<50:
			x+=3
			print("+:",x)

s=Suma()
r=Resta()

s.start()
r.start()
