#Poblado de la base (alumnos)

import sqlite3

conn=sqlite3.connect("Escuela.db")
c=conn.cursor()

print("Ingresa los datos del alumno")
nombre=input("Nombre: ")
apPat=input("Apellido Paterno: ")
apMat=input("Apellido Materno: ")
noCuenta=int(input("Numero de cuenta: "))

c.execute("INSERT INTO alumnos (noCuenta,nombre,apPat,apMat)VALUES(%s,'%s','%s','%s')"%(noCuenta,nombre,apPat,apMat))

for columna in c.execute("SELECT * FROM alumnos"):
	print("id: ",columna[0],"Nombre completo: ",columna[3],columna[4],columna[2],"Numero de cuenta: ",columna[1])

conn.commit()
conn.close()
