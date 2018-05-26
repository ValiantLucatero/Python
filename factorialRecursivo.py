def factorial_recursivo(numero):
    if numero < 2 and numero >= 0:  # Caso base, lo que botará la recursión
        return 1
    return numero * factorial_recursivo(numero-1)  # Operamos recursivamente


print(factorial_recursivo(20))
