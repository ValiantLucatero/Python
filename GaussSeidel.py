import numpy as np

A = np.array([[1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, -1, 1, -1, 0, 0, 0, 0],
              [0, -1, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, -1, 1, 0, 0, 0, 0, 0, 0],
              [0, 10, 0, 0, 0, 0, 1, -1, 0, 0],
              [5, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 5, 0, 0, 0, 0, 1, -1, 0],
              [0, 0, 0, 15, 0, 0, 0, 0, 1, -1],
              [0, 0, 0, 0, 20, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 10, 1, 0, 0, -1]])  # matriz de coeficientes
b = np.array([0, 0, 0, 0, 0, 200, 0, 0, 0, 0])  # matriz de resultados
x0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
print(f"A = {A}")
print(f"b = {b}\n")
n = len(A)  # Devuelve el tamaño de la primera dimensión de la matriz

# Técnicas de Pivoteo
for i in range(n - 1):
    maxV = A[i, i]
    k = i
    for j in range(i + 1, n):
        if abs(A[j, i]) > abs(maxV):
            maxV = A[j, i]
            k = j
    if k != i:
        tempA = np.copy(A[i, :])  # Guardamos Renglón
        A[i, :] = A[k, :]
        A[k, :] = tempA
        tempb = np.copy(b[i])
        b[i] = b[k]
        b[k] = tempb
print("Las nuevas matrices son: \n")
print(f"A = {A}")
print(f"b = {b}")
# La suma de los elementos de la diagonal debe de ser mayor a la de los elementos fuera de esta para que el metodo converga

# Gauss-Seidel
maxIter = 100  # Número máximo de iteraciones
epsilon = 1 * 10**(-8)  # Tolerancia

for k in range(maxIter):
    xi = np.copy(x0)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s = s + A[i, j] * xi[j]
        xi[i] = (1 / A[i, i]) * (b[i] - s)
    e = np.linalg.norm(xi - x0)
    print(f"x{k+1} = {xi}")
    if e < epsilon:
        break
    x0 = np.copy(xi)
