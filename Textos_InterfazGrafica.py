#Textos

from Tkinter import *

root=Tk()

Label(root,
			text="Rojo en Times New Roman",
			fg="red",
			font="Times"
		).pack()
Label(root,
			text="Verde en Helvetica",
			fg="light green",
			bg="dark green",
			font="Helvetica 16 bold italic"
		).pack()
Label(root,
			text="Azul en Verdana",
			fg="blue",
			bg="yellow",
			font="Verdana 10 bold"
		).pack()
root.mainloop()