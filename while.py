#############
# Ciclo While
#############


edad=int(input("\bIngresa tu edad: \n"))
#Si usamos este ciclo while no va a dejar avanzar hasta que ingrese un entero positivo
while edad<0:
	edad=int(input("Porfavor solo edads positivas: "))
#Dejando este bloque fuera del while solo llegarían numeros positovos
if not edad>0:
	print("No se permiten edades negativas")
elif edad<13:
	print("Aún eres un niño")
elif edad >=13 and e<21: # True and True para que se ejecute
	print("Eres un adolecente")
elif edad >=21 and e<100:
	print("Ya estas ruco")
else:
	print("En serio has vivido tanto?")

#Podemos usarlo también para realizar operaciones
n= 100
suma= 0
contador=1

while contador<=100:
	suma=suma+contador
	#suma+=contador
	contador+=1

print("Suma de uno hasta %d: %d" %(n,suma))

#También podemos hacer uso del continue y pass
a=0
while a<10:
	a+=1
	if a==2:
		continue #Termina la iteración pero no rompe el ciclo
		#Si lo cambiamos por pass si imprime el 2
	elif a==5:
		break #Rompe el ciclo en el que se encuentra 
	print(a)

def functionQueHareAlRatoQueMeDenGanas():
	pass #el pass se usa tambien para declaraciones pendientes de programar