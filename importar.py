#########
# Ejemplo de importacion
#########

#import fibo

import fibo as f

print("Ruta de mi archivo: ",f.__file__)
print("Nombre del archivo: ",f.__name__)
print("Documentación: ",f.__doc__)
print("Nombre del modulo: ",f.__module__)
print("Nombre del autor: ",f.__author__)
print("Derechos de autor: ",f.__copyright__)
print("Docstring de Fibonacci",f.Fibonacci.__doc__)
#f.Fibonacci(1000)

#print(f.Fibonacci2(1000))

from fibo import Fibonacci as f1
#from fibo import Fibonacci,Fibonacci2
#rom fibo import *
f1(1500)

#print(Fibonacci2(2800))