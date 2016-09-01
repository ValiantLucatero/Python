import Tkinter as tk

class Ventana1:
	def __init__(self,master):
		self.master=master
		self.frame1=tk.Frame(self.master)
		self.button1=tk.Button(self.frame1,text="Nueva Ventana",width=25,command=self.nuevaVentana)
		self.button1.pack()
		self.frame1.pack()

	def nuevaVentana(self):
		self.nuevaVentana=tk.Toplevel(self.master)
		self.app=Ventana2(self.nuevaVentana)

class Ventana2:
	def __init__(self,master):
		self.master=master
		self.frame2=tk.Frame(self.master)
		self.button2=tk.Button(self.frame2,text="Salir",width=25,command=self.close_windows)
		self.button2.pack()
		self.frame2.pack()
	def close_windows(self):
		self.master.destroy()

def main():
	root=tk.Tk()
	v1=Ventana1(root)
	root.mainloop()

if __name__ == '__main__':
	main()