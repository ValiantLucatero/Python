# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Función


def f(x):
    return (x**2) + 1 - 3 * np.cos(x)


def fp(x):
    return 2 + 3 * np.cos(x)


# Parámetros del Método
a = -10
b = 10
x0 = 0.75

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
epsilon = 1 * 10**(-8)  # Tolerancia

for i in range(maxIter):
    xn = x0 - f(x0) / fp(x0)  # Ecuacion de recurrencia
    e = abs(xn - x0)
    x0 = xn
    if e < epsilon:
        break

print(f"La raíz aproximada es xn = {xn} y se obtuvo con {i+1} iteraciones")
plt.show()
