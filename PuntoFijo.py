# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # Biblioteca de gráficos
import numpy as np  # Biblioteca matemática

# Funciones


def f(x):  # Función original
    return (np.sin(x) / x)**2 - (1 / 2)


def g(x):  # Función G (le sumas x)
    return (np.sin(x) / x)**2 - (1 / 2) + x


def gp(x):  # Derivada de la funcion G
    return (x**3 - 2 * (np.sin(x))**2 + 2 * x * np.sin(x) * np.cos(x)) / x**3


# Parámetros del Método
x0 = 1

# Gráfica de la función
plt.figure(1)
x = np.linspace(-1, 5, 101)
plt.plot(x, f(x), label="$f(x)$")
plt.plot(x, 0 * x, label="Eje x")
plt.title("Punto Fijo")
plt.grid(True)
plt.legend()

# Método
maxIter = 100  # Número máximo de iteraciones
epsilon = 1 * 10**(-4)  # Tolerancia

if gp(x0) < 1:  # Criterio de convergencia
    print("El método converge")
    x = x0
    for i in range(maxIter):
        xn = g(x)
        if abs(xn - x) <= epsilon:
            break
        else:
            x = xn

print(f"La raíz aproximada es xn = {xn} y se obtuvo con {i+1} iteraciones")
plt.show()
