#creamos una clase padre
class Animal():
	def __init__(self,nombre1,peso1):
		self.nombre=nombre1
		self.peso=peso1
	def saludar(self):
		print("Soy un Animal y me llamo ",self.nombre)
class Humano():
	def __init__(self,sexo,edad):
		self.sexo=sexo
		self.edad=edad
	def programar(self):
		print("Soy ",self.sexo," y programo en python")

class Avatar(Humano,Animal):
	def __init__(self,nombre,peso,sexo,edad):
		super().__init__(sexo,edad)
		self.peso=peso
		self.nombre=nombre
		print(self.nombre)
		print(self.sexo)

#creamos una clase terrestre que hereda de Animal
class Terrestre(Animal):
	#creamos el constructor que cuyos dos primeros parametros
	#se pasaran al constructor de la clase padre
	def __init__(self,nombre,peso,patas):
		super().__init__(nombre,peso)
		self.patas=patas
		
	def caminar(self):
			print("Soy un Animal Terrestre y estoy caminando")
			print("tengo ",self.patas," patas")

#a1 = Animal("Dobby",50)
#a1.saludar()
#t1 = Terrestre("Hueso",60,4)
#t1.caminar()
#t1.saludar()
av1 = Avatar("Juan",78,"Masculino",25)
av1.saludar()
av1.programar()

		