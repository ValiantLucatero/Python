##########
# Decoradores
##########


#Son funciones que reciben una funcion como parametro y regresan otra funcion
#Le agregan funcionalidad a la funcion... envuelven a la funcion "decorandola"


def nombre(funcion):
	def decorada(*parametros):
		#acciones nuevas a la funcionalidad
		print("Se ha iniciado la funcion %s"%(funcion.__name__))
		return funcion(*parametros)
	return decorada
#Sin usar el @
def cubo(n):
	return n**3

def suma(a,b):
	print(a+b)

@nombre
def potencia(n,m):
	return n**m

F=nombre(cubo)
print(F(2))
D=nombre(suma)
D(7,3)

print(potencia(2,3))