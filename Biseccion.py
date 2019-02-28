# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # Biblioteca de gráficos
import numpy as np  # Biblioteca matemática

# Función


def f(x):
    return -6765 + 2500 / (1 + x)**1 + 2500 / (1 + x)**2 + 2500 / (1 + x)**3 + 2500 / (1 + x)**4 + 3750 / (1 + x)**5 + 3750 / (1 + x)**6 + 3750 / (1 + x)**7 + 3750 / (1 + x)**8


# Parámetros del Método
a = 0.25
b = 0.50

# Gráfica de la función
plt.figure(1)
x = np.linspace(a, b, 101)
plt.plot(x, f(x), label="$f(x)$")
plt.plot(x, 0 * x, label="Eje x")
plt.title("Bisección")
plt.grid(True)
plt.legend()

# Método
maxIter = 4  # Número máximo de iteraciones
epsilon = 1 * 10**(-8)  # Tolerancia

for i in range(maxIter):
    xm = (a + b) / 2
    print(f"Iteración {i+1} = {xm}")
    e = abs(xm - a)
    if f(a) * f(xm) < 0:
        b = xm
    elif f(b) * f(xm) < 0:
        a = xm
    else:
        break
    if e < epsilon:
        break

print(f"La raíz aproximada es xm = {xm} y se obtuvo con {i+1} iteraciones")
plt.show()
