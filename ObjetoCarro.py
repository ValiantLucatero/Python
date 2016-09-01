class Carro:

	def __init__(self,col,nom,vel):
		self.nombre = nom
		self.color = col
		self.velocidad = vel
	def acelerar(self):
		print("Estoy acelerendo a "+self.velocidad)
	def reversa(self):
		print("Voy en reversa")
	def claxon(self):
		print("Toco el claxon")

c = "Rojo"
n = "Lambo"
v = "210km/h"
car = Carro(c,n,v)

print(car.color)
print(car.nombre)
print(car.velocidad)

car.acelerar()
car.reversa()
car.claxon()