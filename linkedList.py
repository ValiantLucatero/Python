# -*- coding: utf-8 -*-
from Node import Node

# Indicadores
head = None
eraseFirst = False


# Imprime lista
def PrintList():
    if head is None:  # lista vacía
        print("La lista esta vacía")
    else:
        current = head
        while current:
            print(Node.get_data(current), end="  ")  # current.data
            current = Node.get_next(current)  # current.next
        print("")


# Busca nodo
def SearchNode(data):
    previous = head
    global eraseFirst
    if head is None:
        print("La lista está vacía")
    elif Node.get_data(head) is data:  # El número que buscas es el primero
        print(f"{data} si está en la lista! :)")
        eraseFirst = True  # Activamos bandera
        return previous  # En realidad es el actual
    else:
        while (Node.get_next(previous) is not None and
               Node.get_data(Node.get_next(previous)) is not data):  # busca
            previous = Node.get_next(previous)
        if Node.get_next(previous) is None:  # No lo encontró
            print(f"{data} no está en la lista! :(")
            return None
        else:
            print(f"{data} si está en la lista! :)")
            return previous


# Borra nodo
def DeleteNode(previous):
    global head
    global eraseFirst  # elimina todos menos el primero
    if previous is not None and (previous is not head or (previous is head and
                                 eraseFirst is False)):
        erased = Node.get_next(previous)
        Node.set_next(previous, Node.get_next(erased))
        print(f"Se eliminó a {Node.get_data(erased)}")
    elif previous is not None and eraseFirst is True:  # Elimina el primero
        erased = head
        head = Node.get_next(head)
        eraseFirst = False  # Desactivamos bandera
        print(f"Se eliminó a {Node.get_data(erased)}")
    else:
        print("No puedo borrar ese número porque no está en la lista! :O")


# Menú
x = True
while x:
    PrintList()
    x = int(input(
        "Ingresa una opción:\n1)Insertar número\n2)Borrar elemento\n"
        "3)Buscar elemento\n0)Salir\n"))
    if x == 0:
        break
    y = int(input("Ingresa el número: "))
    if x == 1:
        newNode = Node(y)
        Node.set_next(newNode, head)
        head = newNode
    elif x == 2:
        DeleteNode(SearchNode(y))
    elif x == 3:
        SearchNode(y)
    else:
        print("Opción inválida\n")
