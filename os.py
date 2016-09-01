#Modulo OS

import os

print(os.name)

os.system("dir") #windows

os.system("ls") #linux

print(os.getcwd())

print(os.uname()) #linux

print(os.ver) #windows

print(os.listdir(".."))

os.mkdir("Nueva Carpeta")

print(os.chroot("Nueva Carpeta")) #linux, en windows, chdir

print(os.getcwd())

print(chroot(".."))

print(os.rmdir("Nueva Carpeta"))

print(os.listdir("."))