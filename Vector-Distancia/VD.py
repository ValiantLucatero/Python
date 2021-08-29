numeroNodos = 2400
nodoElegido = 101
tiempos = 12

class Nodo():
    def __init__(self, idnodo):
        self.idnodo = idnodo
        self.tabla = {}
        self.vecinos = []
    def addTabla(self, idOtroNodo, pesoarista):
        self.tabla[idOtroNodo] = pesoarista
    def addVecino(self, idVecino):
        self.vecinos.append(idVecino)
    def enviaTabla(self, grafo):
        for vecino in self.vecinos:
            pesoAVecino = grafo[vecino].tabla[self.idnodo] #Obtener peso a ese vecino
            for i in range(1,numeroNodos+1):
                sumaPesos = pesoAVecino + grafo[self.idnodo].tabla[i] #Suma
                if sumaPesos <= grafo[vecino].tabla[i]: #Comparacion
                    grafo[vecino].tabla[i] = sumaPesos #Asignacion
                # Si no es menor, se queda igual
    def printme(self):
        print("ID: ", self.idnodo)
        i = 1
        for v in self.tabla:
            print("N:",v," Peso:",self.tabla[v])
            i += 1

    
if __name__== '__main__':
    f = open("Network19.txt")

    grafo = {}

    l = f.readline()
    while l:
        n = Nodo(int(l.split(':')[0])) #Genera nodos
        for i in range(1,numeroNodos+1): #Genera tabla
            n.addTabla(i, 999999) #Todos los nodos tienen peso infinito
        n.addTabla(n.idnodo,0) #Peso de si mismo es cero
        v = l.split(":")[1].split("-")
        for otroNodo in v:
            if otroNodo.split(",")[0] != "\n":
                idOtroNodo = int(otroNodo.split(",")[0])
                peso = float(otroNodo.split(",")[1])
                n.addTabla(idOtroNodo, peso)
                n.addVecino(idOtroNodo)
        grafo[n.idnodo] = n
        l = f.readline()

    for i in range(1,tiempos+1):
        for i in range(1,numeroNodos+1):
            grafo[i].enviaTabla(grafo)
    grafo[nodoElegido].printme()
