# -*- coding: utf-8 -*-
from Node import Node

# Indicadores
head = None
tail = None
length = 0


# Imprime lista
def PrintList():
    global length
    print("------------------------------------------------------------------")
    if head is None and tail is None:  # lista vacía
        print("La lista esta vacía (no hay nodos)")
    else:
        current = head
        i = 0
        while current:
            print(f"Nodo {i+1}:"+str(Node.get_data(current)), end="  ")
            current = Node.get_next(current)  # current.next
            i = i+1
            length = i
        print("")


# Inserta nodo
def InsertNode(data, position):
    global head, tail
    newNode = Node(data)
    if head is None and tail is None:  # lista vacía
        Node.set_next(newNode, None)
        Node.set_previous(newNode, None)
        head = newNode
        tail = newNode
        print(f"Se ingresó {data} en el Nodo 1")
    else:  # lista con un elemento o más
        current = head
        if position > 0:
            position = position - 1  # ajustamos ya que range inicia en 0
        elif position < 0:
            position = 0  # Ajustamos a numeros negativos
        else:
            pass  # Si es cero, será la nueva cabeza
        for i in range(position):
            if current:
                current = Node.get_next(current)
            else:
                break
        # Lógica con dibujitos
        if current is head:  # Agregarlo al inicio
            Node.set_previous(newNode, None)
            Node.set_previous(head, newNode)
            head = newNode
        elif current is None:  # Agregarlo al final
            Node.set_previous(newNode, tail)
            Node.set_next(tail, newNode)
            tail = newNode
            position = length  # Toma en cuenta numero grandes
        else:  # Agregarlo en medio
            Node.set_previous(newNode, Node.get_previous(current))
            Node.set_next(Node.get_previous(newNode), newNode)
            Node.set_previous(current, newNode)
        Node.set_next(newNode, current)
        print(f"Se ingresó {data} en el Nodo {position+1}")


# Busca nodo
def SearchNode(data):
    if head is None and tail is None:  # lista vacía
        print("No puedes buscar en una lista vacía :/")
    else:
        current = head
        i = 1
        while current and Node.get_data(current) != data:  # Busca
            current = Node.get_next(current)  # current.next
            i = i+1
        if current is None:  # No lo encuentra
            print("El número que buscas no está en la lista :(")
        else:  # Lo encuentra
            print(f"La primera aparicion de {data} es en el nodo {i}")


# Borra nodo
def DeleteNode(position):
    global head, tail, length
    if head is None and tail is None:  # lista vacía
        print("No puedes borrar nada en una lista vacía :/")
    else:
        current = head
        i = 1
        while current and i < position:  # Itera
            current = Node.get_next(current)  # current.next
            i = i+1
        if current is None or position <= 0:  # No hay nada ahí
            print(f"El nodo {position} esta vacío")
        else:  # Si hay algo ahí
            if position == 1:  # Borra la cabeza
                head = Node.get_next(current)
                if length == 1:  # Elimina el último y único elemento
                    head = None
                    tail = None
                    print("Se eliminó el único nodo")
                    return
                Node.set_previous(Node.get_next(current),
                                  Node.get_previous(current))
                print("Se eliminó el nodo 1")
            elif position == length:  # Borra la cola
                tail = Node.get_previous(current)
                Node.set_next(Node.get_previous(current),
                              Node.get_next(current))
                print(f"Se eliminó el nodo {length}")
            else:  # Borra nodo intermedio
                Node.set_next(Node.get_previous(current),
                              Node.get_next(current))
                Node.set_previous(Node.get_next(current),
                                  Node.get_previous(current))
                print(f"Se eliminó el nodo {position}")


# Menú
x = True
while x:
    PrintList()
    op = int(input(
        "Ingresa una opción:\n1)Insertar nodo\n2)Borrar nodo\n"
        "3)Buscar valor en lista\n0)Salir\n"))
    if op == 0:
        break
    if op == 1:
        n = int(input("Elige el nodo: "))
        v = int(input("Ingresa el valor: "))
        InsertNode(v, n)
    elif op == 2:
        n = int(input("Elige el nodo: "))
        DeleteNode(n)
    elif op == 3:
        v = int(input("Ingresa el valor: "))
        SearchNode(v)
    else:
        print("Opción inválida\n")
