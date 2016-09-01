############
# Funciones
############

#def nombrefuncion(parametros):
	#return

def cuadrado(x):
	return x*x

print(cuadrado(5))
print(cuadrado(10))

x=3
y=8.2

def suma(a,b):
	return a+b

resultado=suma(x,y)
print(resultado)

def sumaPrint(a,b):
	print(a+b)

resultado=sumaPrint(x,y)
print(resultado)

def sumaLocal(a,b):
	c=a+b
	return c

resultado=sumaLocal(19,1)
print(resultado)
#print(c)

def resta(a,b):
	return a-b

print(resta(b=4,a=5))
print(resta(b=10,a=5))
#Error... muchos valores para el argumento a
#print(resta(10,a=5))
#resta(3)

#parametros por default

def sumaDefault(a,b=0):
	return a+b

print(sumaDefault(5))
print(sumaDefault(5,5))
print(sumaDefault(2,b=7))

#parametros variables

def sumaMas(a=0,b=0,*otros):
	contador=a+b
	for variable in otros:
		contador+=variable
		#contador=contador+variable
	return contador

print(sumaMas(int(input("Operación:"),int(input("Operación:")))
print(sumaMas(1,1))
print(sumaMas(1,2,3))
print(sumaMas(1,2,3,4,5,6,7,8))

#print(sumaMas(*otros=[3,4,5]))


#regresar mas de un valor

def regresar():
	a=1
	b=3
	return b,a #regresa una tupla

tupla=regresar() #si importa el orden
print(tupla,type(tupla))

A,B=regresar()
print(A) # Contiene-> b
print(B) # Contiene-> a


#Funciones de otros modulos

from math import sqrt

Y=sqrt(256.0)
print(Y)
print(sqrt(sqrt(256.0)))









