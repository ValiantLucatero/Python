##########
# Generadores
##########

def generador():
	yield "1"
	yield "hola"
	yield "siguiente"
	yield 30
	yield [1,2]
	yield (2,3)

a=generador()

print(a.__next__()) #__next__ para python 3
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())#este es el ultimo
#print(a.__next__())



#otro generador

def pares(n):
	a=0
	while n>0:
		if a%2 == 0:
			yield a
			n=n-1
		a=a+1
g=pares(5)
for num in g:
	print(num)

b=pares(5)
for num in b:
	print(num)

