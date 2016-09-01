#definimos la clase Persona
class Persona:
	#agregamos atributos de la clase Persona
	edad = 45
	nombre = "Edgar"

	#definimos un metodo
	def unaFuncion():
		print("Esto es un metodo de clase")
	def saludar(self):
		print("Soy una persona")
		print("Esto es un metodo de instancia")
	def comer(self):
		print("estoy comiendo")
	def estudiar(self):
		print("estoy aprendiendo python")

#instanciamos un objeto de la clase persona
p1 = Persona()
#Accedemos a los atributos de la clase persona
print(p1.edad)
print(p1.nombre)
print(type(p1))
#Accedemos a un metodo de la clase persona
#(metodo de clase)
Persona.unaFuncion()
#accedemos a un metodo de instancia
p1.saludar()
p2 = Persona()
P3 = Persona()
p2.saludar()
P3.estudiar()