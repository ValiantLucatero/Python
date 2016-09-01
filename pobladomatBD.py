#Poblado de la base (materias)

import sqlite3

conn=sqlite3.connect("Escuela.db")
c=conn.cursor()

print("Ingresa una nueva materia: ")

nombre=input("Nombre: ")
clave=int(input("Clave: "))

c.execute("INSERT INTO materias(nombre,clave) VALUES ('%s',%s)"%(nombre,clave))

for columna in c.execute("SELECT * FROM materias"):
	print("id: ", columna[0],"Nombre: ", columna[2], "Clave: ", columna[1])

conn.commit()
conn.close()
