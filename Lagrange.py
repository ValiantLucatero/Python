import numpy as np

# Datos de la función
x = np.array([0, 1, 3, 4])
f = np.array([-6, -2, 54, 142])

# Valor a interpolar
xd = 2

# Cálculo del valor
n = len(x)
fd = 0
for i in range(n):
    L = 1
    for j in range(n):
        if j != i:
            L = L * ((xd - x[j]) / (x[i] - x[j]))
    fd = fd + L * f[i]
print(f"f({xd}) = {fd}")
