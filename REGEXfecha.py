import re
patron="^\d{2}\s\d{2}\s\d{4}$"
fecha=input("Dame una fecha:")

if re.search(patron,fecha):
	print("Se encontro el patron :)")
else:
	print("No se encontro el patron :(")
