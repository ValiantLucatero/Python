import numpy as np
import math as math
# Funcion a integrar


def f(x):
    return math.erf(x)


# Intervalo de integración y número de intervalos
a = 0
b = 4
n = 600  # Debe ser un múltiplo de 2
h = (b - a) / n

# Método numérico
s = f(a) + f(b)
for i in range(1, n):
    if i % 2 == 0:
        s = s + 2 * f(a + i * h)
    else:
        s = s + 4 * f(a + i * h)
s = (h / 3) * s
print(f"El valor de la integral es: {s}")
vr = 4 * math.erf(4) + (np.exp(-4**2)) / (np.sqrt(np.pi))
er = abs((vr - s) / vr)
print(f"El error es: {er}")
