import numpy as np
multPiv = 1  # Contador multiplicador de pivotes


def gauss_jordan(m, eps=1.0 / (10**10)):
    """Pone la matriz ampliada dada en su forma escalonada reducida
     regresa verdadero si es exitoso, falso si la matriz es singular."""
    (h, w) = (len(m), len(m[0]))
    print("Pivotes usados: ")
    global multPiv  # uso de variable global de multiplicacion de pivotes
    for y in range(0, h):
        maxrow = y
        for y2 in range(y + 1, h):    # Encuentra el pivote mayor
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2
        (m[y], m[maxrow]) = (m[maxrow], m[y])
        print(m[y, maxrow])
        multPiv = multPiv * (m[y, maxrow])  # Multiplicador de pivotes
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for y2 in range(y + 1, h):    # Elimina la columna Y
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c
    for y in range(h - 1, 0 - 1, -1):  # Sustitucion
        c = m[y][y]
        for y2 in range(0, y):
            for x in range(w - 1, y - 1, -1):
                m[y2][x] -= m[y][x] * m[y2][y] / c
        m[y][y] /= c
        for x in range(h, w):       # Normaliza  la fila Y
            m[y][x] /= c
    return True


A = np.array([[23.0, 43.0, 6.0, 85.0],  # matriz a resolver
              [11.0, 57.0, 0.0, 23.0],
              [7.0, 8.0, 78.0, 52.0]])

Ared = np.delete(A, A.ndim + 1, A.ndim - 1)  # Matriz no ampliada (sin respuestas)

print("ANÁLISIS NUMÉRICO\nGRUPO:6\nMÉTODO DE ELIMINACIÓN COMPLETA DE GAUSS-JORDAN")
print("Integrantes:\nAlmendarez Estrada Andrea Saraí\nCázares López Jessie Alejandro\nHernández Soriano Luz María\nLucatero Tenorio José Andrés\nMejia Trejo Jaqueline\nPérez Hernández Daniel")

print(f"Matriz a reducir:\n{A}")
if gauss_jordan(A):
    print(f"Matriz escalonada reducida:\n{A}\nDeterminante de la matriz: {np.linalg.det(Ared)}\nMultiplicación de pivotes: {multPiv}")
else:
    print("La matriz es singular y no se puede usar este método")
