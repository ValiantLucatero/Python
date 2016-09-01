#REGEX
import re

# match() search() findall()

patron="python"
cadena="python es un buen lenguaje"

#coincidencia=re.match(patron,cadena)

#print(coincidencia)

#match---> Devuelve algo si el patron esta al inicio
if re.match(patron,cadena):
	print("Se encontro el patron al inicio")
else:
	print("No se encontro el patron al inicio")

#search---> Devuelve algo si esta an cualquier lado
if re.search(patron,cadena):
	print("Se encontro el patron en cualquier lugar")
else:
	print("No se encontro por ningun lado")

#findall()---> Devuelve una lista
lista=re.findall(patron,cadena)
print(lista)