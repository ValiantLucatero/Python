class Persona2:
	#Definimos el constructor de la clase persona
	#este metodo siempre se ejecuta cuando hacemos una instancia de la clase
	def __init__(self,nombre1,apellido1,edad1,estatura1,dinero1):
		self.__nombre=nombre1 #al objeto que estoy creando le asigno nombre1
							#que es lo que recibo
		self.apellido=apellido1
		self.edad = edad1
		self.estatura = estatura1
		self.dinero = dinero1
		print("Hola soy ",self.__nombre," ",self.apellido," ,tengo ",self.edad," años y mido ",self.estatura)

	def comer(self,comida):
		print("Soy ",self.__nombre," y estoy comiendo ",comida)
	def informarSaldo(self):
		print("Soy ",self.__nombre," y cuento con ",self.dinero," pesos.")
	
	def prestarDinero(self,monto,destinatario):
		self.informarSaldo()
		destinatario.informarSaldo()
		if self.dinero > monto:
			self.dinero = self.dinero-monto
			destinatario.dinero=destinatario.dinero+monto
			self.informarSaldo()
			destinatario.informarSaldo()
		else:
			print(self.nombre," No cuentas con el dinero suficiente para prestarle a ",destinatario.nombre)
	
	def getDinero(self):
		return self.dinero
	def setDinero(self,nuevaCantidad):
		self.dinero=nuevaCantidad
	@property
	def __nombre(self):
		return self._nombre
	@__nombre.setter
	def __nombre(self,nombre):
		self._nombre=nombre

p1 = Persona2("Edgar","Huerta",21,1.74,50)
#p1.comer("Tacos")
#p1.informarSaldo()
p2 = Persona2("Alan","Garrido",22,1.80,100)
#p2.prestarDinero(20,p1)
'''
p1.informarSaldo()
p1.setDinero(200)
p1.informarSaldo()
print(p1.nombre," cuenta con ",p1.getDinero()," pesos.")
'''
#llamamos al setter
print(p1._nombre)
p1.comer("Tacos")


