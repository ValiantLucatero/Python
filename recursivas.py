########################
# Funciones Recursivas
########################

#n!

#sin recursividad

def factorialIterativo(n):
	fact=1
	if n==0 or n==1:
		return fact
	else:
		for x in range(1,n+1):
			fact*=x
	return fact	

print(factorialIterativo(0))
print(factorialIterativo(2))
print(factorialIterativo(4000))

#con recursividad

def factorial(n):
	if n<1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(0))
print(factorial(1))
#Se tiene un limite interno de recursividad en python default=1000
print(factorial(4000))


