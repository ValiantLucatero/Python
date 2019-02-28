# -*- coding: utf-8 -*-
import numpy as np  # Biblioteca matemática


def chicharronera():
    print("Ingresa los coeficientes de la ecuación de segundo grado:\n")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = b**2 - 4 * a * c  # Discriminante
    if d < 0:  # Raíces complejas
        x1 = (-b + np.sqrt(-d) * 1j) / (2 * a)
        x2 = (-b - np.sqrt(-d) * 1j) / (2 * a)
        print(f"Las raices son x1 = {x1}, y x2 = {x2}\n")
    elif d == 0:  # Raíces reales iguales
        x1 = (-b) / (2 * a)
        print(f"La raíz es x1 = {x1}\n")
    elif d > 0:  # Raíces reales distintas
        x1 = (-b + np.sqrt(d)) / (2 * a)
        x2 = (-b - np.sqrt(d)) / (2 * a)
        print(f"Las raices son x1 = {x1}, y x2 = {x2}\n")


bandera = 1
while bandera == 1:
    opcion = int(input("Bienvenido, ¿que desea realizar?\n1)Obtener raíces de una ecuación de segundo grado\n0)Salir\n"))
    if opcion == 0:
        print("Adios!")
        bandera = 0
    elif opcion == 1:
        chicharronera()
    else:
        print("Ingresa una opción válida\n")
