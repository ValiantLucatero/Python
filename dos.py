##############
# Otro modulo
##############

import uno

#Podemos ver todo lo que nos llevamos con la funcion dir()
print(dir(uno))
print("Este es el top level de dos.py")


uno.Perro.ladrar()
print(uno.Perro.__doc__)
uno.funcion()
print(uno.otraFuncion.__doc__)
print(uno.lucho.cola)
