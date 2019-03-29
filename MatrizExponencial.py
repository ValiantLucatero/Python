# -*- coding: utf-8 -*-
import numpy as np  # Biblioteca matemática


def ExponentialMatrix(A):
    E = np.zeros(A.shape)  # Genera una matriz de ceros de la misma dimensión que A
    F = np.eye(len(A))  # Genera una matriz identidad de la misma dimensión de A
    k = 1  # Valor de t en e^At
    while np.linalg.norm(E + F - E, 1) > 0:  # Restricción
        E = E + F
        F = A.dot(F) / k
        k = k + 1
    return E


A = np.array([[1.2, 5.6], [3, 4]])
E = ExponentialMatrix(A)
print("Matriz original:\n{}\nMatriz Exponencial:\n{}".format(A, E))
