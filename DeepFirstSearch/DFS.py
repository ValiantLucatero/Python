import sys
sys.setrecursionlimit(5000)

hojas = 0

class Nodo():
    def __init__(self, idnodo):
        self.idnodo = idnodo
        self.visitado = False
        self.vecinos = {}
    def add_vecino(self, idvecino, pesoarista):
        self.vecinos[idvecino] = pesoarista
    def printme(self):
        print("ID: ", self.idnodo)
        i = 1
        for v in self.vecinos:
            print("V"+str(i)+":",v," Peso:",self.vecinos[v])
            i += 1


def DFS(grafo, raiz, arbol):
    global hojas
    n = grafo[raiz]
    n.visitado = True
    nodo = Nodo(raiz)
    bandera = False #Checa si hay vecinos sin visitar---------------------------------------
    for v in n.vecinos:
        if grafo[v].visitado == False:
            bandera = True #Con que tenga 1 vecino sin visitar se cambia--------------------
            nodo.add_vecino(v,1)
            DFS(grafo, v, arbol)
    if bandera == False: #Si itero a traves de todos los vecinos y todos estaban visitados--
        hojas += 1 #Es una hoja-------------------------------------------------------------
    arbol.append(nodo)
        
    
if __name__== '__main__':
    f = open("midResult.txt")

    grafo= {}
    arbol= []

    l = f.readline()
    while l:
        n = Nodo(l.split(':')[0])
        v = l.split(":")[1].split("-")
        for vecino in v:
            idvecino = vecino.split(",")[0]
            peso = float(vecino.split(",")[1])
            n.add_vecino(idvecino, peso)
        grafo[n.idnodo] = n
        l = f.readline()

    DFS(grafo, "391", arbol)

    print("Hojas:", hojas) # Primera pregunta resuelta-----------------------------------------

    # Segunda pregunta resuelta-----------------------------------------------------------------
    numeroHijos = 0
    maxNumeroHijos = 0
    papasGrandes = []
    
    for a in arbol:
        numeroHijos = len(a.vecinos)
        if numeroHijos > maxNumeroHijos:
            maxNumeroHijos = numeroHijos #Obtiene el maximo numero de hijos de cualquier nodo

    for a in arbol:
        numeroHijos = len(a.vecinos)
        if numeroHijos == maxNumeroHijos:
            papasGrandes.append(int(a.idnodo)) #Obtiene que nodos tienen el maximo numero de hijos
            
    print(max(papasGrandes),"es el nodo mas grande con mas hijos (",maxNumeroHijos,")")
    print(min(papasGrandes),"es el nodo mas chiquito con mas hijos (",maxNumeroHijos,")")
    #-------------------------------------------------------------------------------------------
    #Cantidad de nodos con mas de 1 hijo
    numeroHijos = 0
    numeroPapasMultiples = 0

    for a in arbol:
        numeroHijos = len(a.vecinos)
        if numeroHijos > 1:
            numeroPapasMultiples += 1 #Cuenta cuantos nodos tienen mas de 1 hijo
    
    print(numeroPapasMultiples,"nodos tienen mas de 1 hijo")