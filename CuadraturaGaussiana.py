import numpy as np
import scipy.special as sp
from sympy import *
x = symbols('x')

# Función a integrar


def f(x):
    return np.sin(x) + np.exp(x)


def F(x):
    return -np.cos(x) + np.exp(x)


# Intervalo de integración
a = 0
b = 100
n = 3  # Grado del polinomio


# Polinomios de Legendre
def p(n):
    p = 0
    for k in range(n + 1):
        p = p + (sp.binom(n, k)**2) * (x + 1)**(n - k) * (x - 1)**k
    p = expand((1 / 2)**n * p)
    return p


# Raíces de p_n
pn = p(n)
xi = solve(pn, x)

# Derivada del polinomio
pnp = diff(pn, x)

# Pesos w_i e integración
s = 0.0
wi = 0.0 * np.zeros(n)
for i in range(n):
    wi[i] = 2 / ((1 - xi[i]**2) * pnp.subs(x, xi[i])**2)
    s = s + wi[i] * f(float((b - a) / 2 * xi[i] + (a + b) / 2))
s = (b - a) / 2 * s
print(f"La aproximación de la integral es: {s}")
vr = F(b) - F(a)
er = abs((vr - s) / vr)
print(f"El error es: {er}")
