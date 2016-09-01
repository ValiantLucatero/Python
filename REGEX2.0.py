#REGEX 2.0 METACARACTERES
import re

#Ejemplos:
# . Coincide con cualquier cosa (Excepto salto de linea)
# * Cerradura Estrella (0 o mas coincidencias)
# $ Final de cadena
# ^ Inicio de la cadena
# + Cerradura positiva (1 o mas veces)
# ? Puede aparecer 0 o 1 vez

#patron="..s."
#cadena="12so"
patron="a*b"
cadena="aaaaaaaaaaaab"

if re.search(patron,cadena):
	print("Se encontro el patron")
else:
	print("No se encontro")