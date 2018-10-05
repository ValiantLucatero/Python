"""Reto 1."""
import re
f = open("texto.txt", "r")
f.seek(0)
cadena = f.read()
f.close()
tupla = re.subn("\s", "", cadena)
lista = ()
lista = list(tupla)
print(lista)
