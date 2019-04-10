from scipy import linalg, array

A = array([[7, 3, -1, 2],
           [3, 8, 1, -4],
           [-1, 1, 4, -1],
           [2, -4, -1, 6]])

P, L, U = linalg.lu(A)

print(f"A:{A}")
print(f"P:{P}")
print(f"L:{L}")
print(f"U:{U}")
