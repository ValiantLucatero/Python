import numpy as np
import math as math
# Funcion a integrar


def f(x):
    return np.sin(x) + x * np.exp(x) + np.log(x)


def F(x):
    return np.exp(x) * (x - 1) - x + x * np.log(x) - np.cos(x)


# Intervalo de integración y número de intervalos
a = 2
b = 3
n = 8  # Debe ser un múltiplo de 3
h = (b - a) / n
# Método numérico
s = f(a) + f(b)
for i in range(1, n):
    if i % 3 == 0:
        s = s + 2 * f(a + i * h)
    else:
        s = s + 3 * f(a + i * h)
s = (3 * h / 8) * s
print(f"El valor de la integral es: {s}")
vr = F(b) - F(a)
er = abs((vr - s) / vr)
print(f"El error es: {er}")
