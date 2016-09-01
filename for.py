##############
# ciclo For
##############

#Podemos usar la función range que tiene la sintaxis range(inicio,fin,salto)
#Del 0 al 9
for i in range(10):
	print(i)
#Del 5 al 9
for x in range(5,10):
	print(x)
#Del 2 al 10 de dos en dos
for x in range(2,10,2):
	print(x)

for x in range(9,0,-1):
	print(x)

#Podemos iterar sobre objetos indexables
#Como cadenas
cadena="Python"

for letra in cadena:
	print(letra,end=" ")

#Listas
lenguajes=["Python","C","Java"]

for lenguaje in lenguajes:
	print(lenguaje)
#Y tuplas
frutas=("manzana","uva","pera")

#Ademas podemos usar otros bloques dentro de este mismo
#Claro con su respectiva identacion
frutasQueMegusta=[]
for fruta in frutas:
	if(fruta=="uva"):
		print(fruta)
		break
	else:
		print("no me gusta")
