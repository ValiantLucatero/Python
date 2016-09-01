#Decorador que quite los numeros repetidos de una lista


def quitaRepetido(funcion):
	def funDecorada(*parametros):
		print("Decorador quitaRepetido:")
		lista=funcion(*parametros)
		print("Lista original: ",lista)
		nuevaLista=[]
		for elemento in lista:
			n=True
			for repeticion in nuevaLista:
				if repeticion == elemento:
					n=False
			if n==True:
				nuevaLista.append(elemento)
		print("ya acabamos!!! Lista sin repetidos: ",nuevaLista)
	return funDecorada

@quitaRepetido
def sumaListas(li1,li2):
	return list(map(lambda a,b: a+b,li1,li2))

a=[1,5,1,5,1,3,1,2,7]
b=[3,2,3,2,3,2,3,2,3]

sumaListas(a,b)



