import numpy as np
from scipy.linalg import lu_factor, lu_solve
A = np.array([[120, -20, 0],
              [-80, 80, 0],
              [-40, -60, 120]])
b = np.array([500, 0, 200])
lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)
print("Soluciones: ")
print(x)
