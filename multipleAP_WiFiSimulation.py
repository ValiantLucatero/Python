import random
import matplotlib.pyplot as plt

#Variables
numberOfNodes = 10 #2 or 10
data = 1500 #bytes
dataSendTime = (data * 8)/1000000 #1 Mbps
ack = 60 #bytes
ackSendTime = (ack * 8)/1000000 #1 Mbps
DIFS = 0.000264 #264 microseconds
SIFS = 0.00016 #160 microseconds
time = 0
ShortJump = DIFS
LongJump = dataSendTime + SIFS + ackSendTime

class Node:
    def __init__(self):
        self.EB = 100 #Default value, will be changed.
        self.sentPackages = 0
        self.collisions = 0
        self.recentlyCollided = 0
        self.EB_History = []

    def setNewEB(self,EB):
        self.EB = EB
        self.EB_History.append(self.EB)

    def reduceEB(self):
        self.EB -= 1

    def getEB(self):
        return self.EB

    def addSentPackage(self):
        self.sentPackages += 1
    
    def getSentPackages(self):
        return self.sentPackages

    def setRecentlyCollided(self, value):
        self.recentlyCollided = value

    def getRecentlyCollided(self):
        return self.recentlyCollided

    def addCollision(self):
        self.collisions += 1
    
    def getCollisions(self):
        return self.collisions
    
    def getEBmean(self):
        return sum(self.EB_History)/len(self.EB_History)

    def printNodesInfo(self, index):
        print("-----------------------------------------------\nInformación del nodo",
        index,":\nExponential Backup promedio =",self.getEBmean(),"\nPaquetes Enviados =",
        self.sentPackages,"\nThroughput =",((self.sentPackages*data*8)/time)/1000,
        "Kbps\nColisiones =",self.collisions,"\n-----------------------------------------------")

#Create nodes
NodesList = [Node() for _ in range(numberOfNodes)]

#Assign first EBs
[node.setNewEB(random.randrange(0,16)) for node in NodesList]

#TransmissionCycle
#While no one has been able to send 1000 packages...
while [node.getSentPackages() for node in NodesList].count(1000) == 0:

    if [node.getEB() for node in NodesList].count(0) == 1:
        sendingNode = [node.getEB() for node in NodesList].index(0)
        NodesList[sendingNode].addSentPackage()
        NodesList[sendingNode].setNewEB(random.randrange(0,16))
        NodesList[sendingNode].setRecentlyCollided(0) #Managed to transmit, eliminate flag
        print("(",time,"seg.): El nodo",sendingNode,"inicia transmisión, se hace un Salto Largo")
        time += LongJump

    elif [node.getEB() for node in NodesList].count(0) > 1: #Collission detected!
        print("(",time,"seg.): Se inicia transmisión de múltples nodos, se hace un Salto Largo")
        time += LongJump
        print("(",time,"seg.): Colisión detectada! Se aumenta ventana de los nodos involucrados")
        collidingNodes = [index for index, node in enumerate(NodesList) if node.getEB() == 0]
        for index in collidingNodes: #Modify each involved node
            RecentCollisions = NodesList[index].getRecentlyCollided()
            NodesList[index].setNewEB(random.randrange(0,2**(5+RecentCollisions))) #Make window bigger
            NodesList[index].setRecentlyCollided(RecentCollisions + 1) #Add marking of collision
            NodesList[index].addCollision() #Sum to total number of collisions
            print("El nodo",index,"ha colisionado",RecentCollisions + 1,"vez/veces!")
            print("Aumentando la ventana a [ 0 -",2**(5+RecentCollisions),"]")

    elif [node.getEB() for node in NodesList].count(0) == 0:
        print("(",time,"seg.): Ningún EB es igual a cero, se hace un Salto Corto")
        time += ShortJump
        [node.reduceEB() for node in NodesList] #All EBs are substracted 1

fastestNode = [node.getSentPackages() for node in NodesList].index(1000)
print("El nodo",fastestNode,"logró enviar 1000 paquetes con éxito en",time,"segundos")
[node.printNodesInfo(NodesList.index(node)) for node in NodesList] #Print node's info

#Plots

#Throughput plot
throughputData = [((node.getSentPackages()*data*8)/time)/1000 for node in NodesList]
TH = plt.figure(1)
plt.bar(range(len(throughputData)), throughputData, color='royalblue', alpha=0.7)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(range(len(throughputData)), list(range(len(throughputData))))
plt.xlabel('Nodos')
plt.ylabel('Kbps')
plt.title('Throughput en Kbps')

#Collisions plot
collisionsData = [node.getCollisions() for node in NodesList]
CL = plt.figure(2)
plt.bar(range(len(collisionsData)), collisionsData, color='violet', alpha=0.7)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(range(len(collisionsData)), list(range(len(collisionsData))))
plt.xlabel('Nodos')
plt.ylabel('Colisiones')
plt.title('Número de colisiones de cada nodo')
plt.show()