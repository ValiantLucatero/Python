##############
# Switch-case
##############

'''
caso=int(input("Dame un #: "))

if caso==0:
	print("usted escribió cero")
elif caso==1 or caso==9 or caso==4:
	print("Usted escribió un cuadrado perfecto")
elif caso%2 == 0:
	print("Usted escribió un número par")

#def nombrefuncion(parametros):

def zero():
	print("usted escribió cero")

def impar():
	print("usted escribió un impar")

def par():
	print("usted escribió un par")

opciones={
	0:zero,
	1:impar,
	2:par
}
 #acceder a un diccionario de funciones
caso=int(input("Dame un #: "))
opciones[caso]()
'''

diccionario={1:"Opcion 1",2:"Opcion 2",3:"Opcion 3"}
lista=list(diccionario.keys())

while True:
	for llave in lista:
		print("\t%s. %s" % (llave,diccionario[llave]))
	seleccion=int(input("Selecciona una opcion: "))
	if seleccion in lista:
		print("Seleccionaste la ",diccionario[seleccion])
		#break
	else: #default
		print("Opción inválida")






