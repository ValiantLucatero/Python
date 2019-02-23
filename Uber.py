#Sistema Uber

from Tkinter import *
import time
import locale

root=Tk()

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dia = time.strftime("%A")
NumDia = time.strftime("%d")
mes = time.strftime("%B")
CostoUber=Entry(root)
Comis=IntVar()

Label(root,text = dia).grid(row=0)
Label(root,text = NumDia).grid(row=0,column=1)
Label(root,text = "de "+mes).grid(row=0,column=2)
CostoUber.grid(row=0,column=3)
Label(root,text = "Costo Uber").grid(row=1,column=3)
R1 = Radiobutton(root, text="10%", variable=Comis, value=.10).grid(row=0,column=4)
R2 = Radiobutton(root, text="25%", variable=Comis, value=.25).grid(row=1,column=4)
R3 = Radiobutton(root, text="30%", variable=Comis, value=.30).grid(row=2,column=4)

root.mainloop()
