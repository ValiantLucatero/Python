#Secuencias

#\d Numeros					\D No numeros
#\w Alfanumericos			\W No alfanumericos
#\s caracteres en blanco	\S No caracteres en blanco

# {} contador				() Grupos
# | "or"
import re

patron="^(ab)+$"
cadena="ababab"

if re.search(patron,cadena):
	print("Se encontro el patron en la cadena")
else:
	print("No se encontro el patron")
