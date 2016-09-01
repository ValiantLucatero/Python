#datos intermedios

import sqlite3

conn=sqlite3.connect("Escuela.db")

c=conn.cursor()

print("INSCRIBIR MATERIAS")

noCuenta=input("Numero de cuenta: ")
idAlumno=0

for columna in c.execute("SELECT * FROM alumno WHERE noCuenta='%s'"%(NoCuenta)):
	print("id: ",columna[0],"Nombre Completo: ",columna[2],columna[3],columna[4],'No cuenta: ',columna[1])

for columna in c.execute("SELECT * FROM materias"):
	print("id: ",columna[0],"Nombre: ",columna[1],'Clave: ',columna[2])

idMateria=int(input("Ingresa el id de la materia a inscribir: "))

c.execute("INSERT INTO alumnosmaterias(alumnos_idalumnos,materias_idmaterias)VALUES(%s,%s)"%(idAlumno,idMateria))

print("MATERIA INGRESADA CON EXITO")

for columna in c.execute("SELECT * FROM alumnos,materias,alumnosmaterias WHERE noCuenta= '%s' AND alumnosmaterias.alumnos_idalumnos=alumnos.idalumno AND alumnosmaterias.materias_idmaterias=materias.idmaterias"%(noCuenta)):
	print(columna)

conn.commit()
conn.close()
