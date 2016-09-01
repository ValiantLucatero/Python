#########
# modulos en python
#########


class Perro():
	"""Linea de documentacion para Perro"""
	def __init__(self, patas,dientes,cola):
		self.patas=patas
		self.dientes=dientes
		self.cola=cola
	def ladrar():
		print("Woof!!!!")
	def correr(self):
		print("Soy un perro que corre con: ",self.patas,"patas")

def funcion():
	print("funcion() en uno.py")

print("Este es el top level de uno.py en el top level")

if __name__ == '__main__':
	#todo lo que este dentro de este if no se importa!!
	print("uno.py esta corriendo directamente")
	lucho=Perro(4,20,"esponjada")

#else:
#	print("uno.py esta siendo importado por otro modulo")

def otraFuncion():
	"""docstring"""
	print("Esta funcion tambien se importa")



