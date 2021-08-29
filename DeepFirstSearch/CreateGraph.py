import math

class Nodo():
    def __init__(self, idnodo, x, y):
        self.idnodo = idnodo
        self.visitado = False
        #self.vecinos = []    #Es una lista
        self.vecinos = {}
        self.x = x
        self.y = y
    def add_vecino(self, idvecino, pesoarista):
        #self.vecinos.append((idvecino, pesoarista))
        self.vecinos[idvecino] = pesoarista
    def printme(self):
        print("ID: ", self.idnodo)
        i = 1
        for v in self.vecinos:
            print("V"+str(i)+":",v," Peso:",self.vecinos[v])
            i += 1
        
    
if __name__== '__main__':
    f = open("Network1.txt")

    grafo= {} # Vector de nodos (con sus coordenadas)
    arbol= []

    # Cargamos todos los nodos en RAM
    l = f.readline()
    while l: 
        x = l.split(":")[1].split("(")[1].split(",")[0]
        y = l.split(":")[1].split(",")[1].split(")")[0]
        n = Nodo(l.split(':')[0], x, y)
        grafo[n.idnodo] = n
        l = f.readline()

    # Buscaremos los vecinos de cada nodo para armar el grafo
    for idnodo in grafo:
        for idvecino in grafo:
            ecDistance = math.sqrt((float(grafo[idvecino].x) - float(grafo[idnodo].x))**2 + (float(grafo[idvecino].y) - float(grafo[idnodo].y))**2) # Distancia euclideana del nodo a cada uno de los otros nodos
            if ecDistance != 0.0 and ecDistance < 100: # No entra si es el mismo nodo o esta muy lejos
                peso = ecDistance
                grafo[idnodo].add_vecino(int(idvecino), peso)
    
    # Criterios de desempate>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #De menor a mayor indice YA ESTA------------------------------------------------------------------
    #De mayor a menor indice--------------------------------------------------------------------------
    #for idnodo in grafo:
        #grafo[idnodo].vecinos = dict(sorted(grafo[idnodo].vecinos.items(), key=lambda item: item[0], reverse = True))
    #De mayor peso a menor peso-----------------------------------------------------------------------
    #for idnodo in grafo:
        #grafo[idnodo].vecinos = {key: value for key, value in sorted(grafo[idnodo].vecinos.items(), key=lambda item: item[1],reverse=True)}
    #De menor peso a mayor peso-----------------------------------------------------------------------
    #for idnodo in grafo:
        #grafo[idnodo].vecinos = {key: value for key, value in sorted(grafo[idnodo].vecinos.items(), key=lambda item: item[1])}
    #De mayor numero de vecinos a menor numero de vecinos---------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Escribimos el archivo con el grafo armado
    g = open("midResult.txt", "w")
    for idnodo in grafo:
        string = grafo[idnodo].idnodo + ":"
        for v in grafo[idnodo].vecinos:
            string = string + str(v) + "," + str(grafo[idnodo].vecinos[v]) + "-"
        if len(string) >= 5: # Si el nodo tiene vecinos quitamos el dash final
            string = string[:-2] + "\n"
        else: #Si no tiene vecinos no hay dash que quitar
            string = string + "\n"
        g.write(string)

    #print(grafo)

    #for nodo in grafo:
    #    grafo[nodo].printme()