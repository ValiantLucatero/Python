import numpy as np
from scipy import linalg


def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)


def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break

        v = v_new
        ev = ev_new
    return ev_new, v_new


A = np.array([[4, 2, -2],
             [-5, 3, 2],
             [-2, 4, 1]])

AInv = linalg.inv(A)

print(f"Matriz a trabajar:\n{A}")
print(f"Inversa:\n{AInv}")
print("Ultimo valor de lambda (MAYOR):")
print(power_iteration(A))
print("Ultimo valor de lambda (MENOR):")
print(power_iteration(AInv))  # no da bien bien
