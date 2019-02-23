import matplotlib.pyplot as plt
import numpy as np

#Función
def f(x):
    return np.log(x)-0.5

#Parámetros del Método
a=1
b=2

#Gráfica de la función
plt.figure(1)
x = np.linspace(a,b,101)
plt.plot(x,f(x),label="$f(x)$")
plt.plot(x,0*x,label="Eje x")
plt.title("Falsa Posicion")
plt.grid(True)
plt.legend()

#Método
maxIter=100 #Número máximo de iteraciones
epsilon=1*10**(-8) #Margen de error

for i in range(maxIter):
    xm=a+(f(a))/(f(a)-f(b))*(f(b)-f(a))
    e=abs(xm-a)
    if f(a)*f(xm)<0:
        b=xm
    elif f(b)*f(xm)<0:
        a=xm
    else:
        break
    if e<epsilon:
        break
        
print(f"La raíz aproximada es xm = {xm} y se obtuvo con {i+1} iteraciones")
plt.show()
