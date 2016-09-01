################
# lambdas
################


funcion=(lambda a,b:a+b)
print(funcion(3,3))

#map() aplica una funcion a cada uno de los elementos de una lista
#devuelve una nueva lista

lista1=[1,2,3,4,5,6]

lista2=list(map(lambda n:n**2,lista1))

print(lista2)
print(lista1)

def cuadrado(n):
	return n**2

lista3=list(map(cuadrado,lista1))

print(lista3)


#filter() aplica una funcion solo su cumple con una condicion 
#si es falsa no agrega el valor a la nueva lista

li2=list(filter(lambda n: n%2==0,lista1))
print(li2)

#reduce() aplica a dos elementos de una lista, los remueve y añade
#el nuevo valor obtenido por la funcion, y sigue así hasta que solo haya uno

import functools

li3=functools.reduce(lambda a,b:a+b,lista1)
print(li3)