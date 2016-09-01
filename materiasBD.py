#BD escuela (creacion de BD)

import sqlite3

#conectar base de datos
conn=sqlite3.connect("Escuela.db")


#crear cursor para ejecutar comandos sql
c=conn.cursor()

#ejecutar pasos para crear tablas para que no se sobrepongan

try:
	c.executescript("DROP TABLE alumnos, materias, alumnomaterias")

except:
	print("La base de datos ha sido borrada anteriormente")


#CREAR TABLAS

try:
	c.execute("CREATE TABLE alumnos(idalumnos INTEGER PRIMARY KEY, noCuenta INTEGER, nombre TEXT, apPat TEXT, apMat TEXT)")
	print("Tabla alumnos creada")

except:
	print("La tabla ya existe")

try:
	c.execute("CREATE TABLE materias(idmaterias INTEGER PRIMARY KEY, clave INTEGER, nombre TEXT)")
	print("Tabla materias creada")

except:
	print("La tabla ya existe")

try:
	c.execute("CREATE TABLE alumnosmaterias(alumnos_idalumnos INTEGER, materias_idmaterias INTEGER, FOREIGN KEY(alumnos_idalumnos)REFERENCES alumnos(idalumnos), FOREIGN KEY (materias_idmaterias)REFERENCES materias(idmaterias) )")
	print("Tabla intermedia creada")
except:
	print("La tabla ya existe")

conn.commit()
conn.close()
