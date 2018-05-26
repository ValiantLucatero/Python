# Este ejemplo ha sido tomado de
# http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
tess = turtle.Turtle()
tess.shape("classic")
tess.color("blue")
size = 20
'''
for i in range(4):  # Forma iterativa
    tess.forward(99)  # La tortuga avanza
    tess.right(90)  # Gira 90 grados
    tess.stamp()  # Deja la forma de la tortuga en las esquinas
'''


def cuadrado(lado):  # Forma recursiva
    if lado > 0:
        tess.forward(99)
        tess.right(90)
        cuadrado(lado-1)


cuadrado(4)
wn.mainloop()
