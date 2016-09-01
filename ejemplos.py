################
# Ejemplos
################

#Establecemos un rango de 1 a 3
num=range(1,4)

#Para crear nuestra matriz  solo ponemos una lista [[]]
#detro de otra e iteramos en las dos
matrix=[[0 for i in num]for j in num]

print(matrix[0])
print(matrix[1])
print(matrix[2])

###Matriz de coordenadas

#En la matriz podemos colocar cualquer objeto, siempre que cumpla
#con  la especificacion que le damos
matrix2=[[(i-1,j-1)for i in num]for j in num]
print(matrix2[0])
print(matrix2[1])
print(matrix2[2])


##Generador de numeros primos

def primos():
	primo=[]
	a=2.0
	while True:
		enc=False
		for p in primo:
			if a%p==0:
				enc=True
		if enc==False:
			primo.append(a)
			yield a
		a+=1

a=primos()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

#La suma de los primeros 5 primos
import functools
p=primos()
#Lo que se hace en esta linea es mandar a la funcion reduce
#que recibe como parámetros una funcion lambda que solo suma los elementos
#y una lista por comprensión que devuelve el siguiente del generador de primos de 1 a 5
sumaP=functools.reduce(lambda a,b: a+b, [ p.__next__() for n in range(1,6)] )
print(sumaP)
