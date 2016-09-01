############
# do while
############

#El ciclo infinito es para que lo haga al menos una vez
while True:
	print("Esto al menos se imprime una vez")
	a=int(input("Escribe cero para romper el ciclo: "))
	if a==0: #planteamos la condición a la cual queremos que termine el ciclo
		break
	print("Terminar") #Eso no se ejecuta porque el break rompe el bloque