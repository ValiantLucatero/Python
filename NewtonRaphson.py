# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # Biblioteca de gráficos
import numpy as np  # Biblioteca matemática

# Función y sus derivadas


def f(x):  # Función original
    return ((np.pi * x**2) * (3 - x)) / (0.5 * 3)


def fp(x):  # Primera derivada
    return x * (12.5664 - (6.28319 * x))


def fpp(x):  # Segunda derivada
    return 12.5664 - (12.5664 * x)


# Parámetros del Método
a = 2
b = 4
x0 = 5

# Gráfica de la función
plt.figure(1)
x = np.linspace(a, b, 101)
plt.plot(x, f(x), label="$f(x)$")
plt.plot(x, 0 * x, label="Eje x")
plt.title("Newton-Raphson")
plt.grid(True)
plt.legend()

# Método
maxIter = 100  # Número máximo de iteraciones
epsilon = 1 * 10**(-4)  # Tolerancia

if abs((f(x0) * fpp(x0)) / (fp(x0))**2) < 1:  # Criterio de convergencia
    print("Converge")
    for i in range(maxIter):
        xn = x0 - f(x0) / fp(x0)  # Ecuacion de recurrencia
        print(f"Iteración {i+1} = {xn}")
        e = abs(xn - x0)
        x0 = xn
        if e < epsilon:
            break
else:
    print("No converge")

print(f"La raíz aproximada es xn = {xn} y se obtuvo con {i+1} iteraciones")
plt.show()
