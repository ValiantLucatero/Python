import re
patron="^[a-z0-9_\.\-]+@[a-z0-9]{5,15}\.(com|com.mx|unam.mx)"
correo=input("Dame un correo:")

if re.search(patron,correo):
	print("Se encontro el patron :)")
else:
	print("No se encontro el patron :(")
