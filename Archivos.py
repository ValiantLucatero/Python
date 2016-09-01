#Archivos

f= open("texto.txt","w+") #Write, Read(sobre-escribe), Append(al final de lo escrito)[si les agregas + pueden leer y escribir]; rb(leer binarios), wb(sobre-escribir binario), ab(al final del binario) 

print("Nombre del archivo: ",f.name)
print("Modo de apertura: ",f.mode)

#f.close()
if f.closed:
	print("El archivo se ha cerrado")
else:
	print("el archivo sigue abierto")

texto= input("Ingrese texto para escribir en el archivo: ")
texto+='\n'

f.write(texto)

#f.close()

print(f.tell())

f.seek(0)

print(f.tell())

cadena=f.read()

print("La cadena leida fue: ",cadena)