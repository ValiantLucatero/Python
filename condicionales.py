##################
# Control de flujo
##################

edad=int(input("Dime tu edad: "))


if not edad>0:
	print("No se permiten sedades negativas")
elif edad<13:
	print("Aún eres un niño")
elif edad >=13 and edad<21: # Tienen que ser verdaderas las dos condiciones
	print("Eres un adolecente")
elif edad >=21 and edad<100:
	print("Ya estas ruco")
else: #Si no se cumple cualquiera de los otros casos
	print("En serio has vivido tanto?")

if edad % 3 == 0 or edad % 5 == 0: #Solo una de las condiciones tiene que ser verdadera
	print("El numero que ingresaste es divisible entre 3 o 5")



#Podemos buscar por la existencia en algún objeto indexable como las listas 

lista=[1,2,3,4,5,6,7]
if 4 in lista: #busca hasta que encuentra la primer ocurrencia
	print("Hay un 4 en la lista")
else:
	print("No hay un cuatro en la lista")


	
