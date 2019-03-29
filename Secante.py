# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # Biblioteca de gráficos
import numpy as np  # Biblioteca matemática


# Función
def f(x):  # Función original
    return np.exp(x) - (3 * x)


# Parámetros del Método
a = 1.4
b = 1.6

# Gráfica de la función
plt.figure(1)
x = np.linspace(a, b, 101)
plt.plot(x, f(x), label="$f(x)$")
plt.plot(x, 0 * x, label="Eje x")
plt.title("Secante")
plt.grid(True)
plt.legend()

# Método
maxIter = 100  # Número máximo de iteraciones
epsilon = 1 * 10**(-8)  # Tolerancia
xn = (a + b) * (0.5)

for i in range(maxIter):
    xn = b - ((b - a) / (f(b) - f(a))) * f(b)  # Ecuacion de recurrencia
    a = b
    b = xn
    print(f"Iteración {i+1} = {xn}")
    e = abs(f(xn))
    if e < epsilon:
        break

print(f"La raíz aproximada es xn = {xn} y se obtuvo con {i+1} iteraciones")
plt.show()
