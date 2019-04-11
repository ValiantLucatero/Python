import numpy as np
# Con dos  o tres números
# Datos de la funcion
x = np.array([0.0, 1, 2])
y = x**2 + 4 * x - np.pi  # Puede ser los valores: np.array([-2, 3])
h = x[1] - x[0]
if len(x) == 2:
    yp = (1 / h) * (y[1] - y[0])  # A lo que le restas es de lo que obtienes la derivada (y[0])
    print(f"f'({x[0]}) = {yp}")
elif len(x) == 3:
    yp = (1 / 2 * h) * (y[2] - y[0])  # El valor entre los dos que restas es de lo que obtienes la derivada (y[1])
    print(f"f'({x[1]}) = {yp}")
