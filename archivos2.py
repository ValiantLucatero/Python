#Leer archivos

archivo=input("Dame el nombre del archivo: ")

with open(archivo) as f:
	lineas=f.readlines()

print(lineas)

lineas = [linea.rstrip('\n') for linea in open(archivo)] #el rstrip es para quitarles un caracter en especial

print(lineas)

with open("nuevo.txt","w") as f:
	f.write(lineas)