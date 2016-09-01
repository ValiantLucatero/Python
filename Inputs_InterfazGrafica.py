#!/usr/bin/env python
#Entrada de datos

from Tkinter import *

root=Tk()
Label(root,text="Nombre: ").grid(row=0)
Label(root,text="Apellido Paterno: ").grid(row=1)
Label(root,text="Apellido Materno: ").grid(row=2)

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

def mostrarCampos():
	print("Hola: ",e1.get(),e2.get(),e3.get())
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)

Button(root,text="Salir",command=root.quit).grid(row=3,column=0,sticky=W,pady=4)
Button(root,text="Mostrar",command=mostrarCampos).grid(row=3,column=1,sticky=W,pady=4)
root.mainloop()
