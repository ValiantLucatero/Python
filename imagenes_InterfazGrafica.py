#Imagenes

from Tkinter import *

root=Tk()
logo=PhotoImage(file="13428639_1131057286939952_361989741583329412_n.png")
lb1=Label(root,image=logo).pack(side="right")
description="Uso de imagenes, curso de Python Intermedio"
lb2=Label(root,text=description,justify=LEFT,padx=10).pack(side="left")
root.wm_title("Uso de imagenes")

root.mainloop()