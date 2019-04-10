from scipy import array
from scipy.optimize import newton_krylov

A = array([[7, 3, -1, 2],
           [3, 8, 1, -4],
           [-1, 1, 4, -1],
           [2, -4, -1, 6]])

B = array([0, 0, 0, 0, 0])

x = newton_krylov(A, B)  # Espera que su primer argumento sea una función f(x)=Ax+b

print(x)
