import random

data = 1500 #bytes
dataSendTime = (data * 8)/1000000 #1 Mbps
ack = 60 #bytes
ackSendTime = (ack * 8)/1000000 #1 Mbps
numberOfPackages = 1000 #1000
DIFS = 0.000264 #264 microseconds
SIFS = 0.00016 #160 microseconds
EB_History = []
time = 0
timer = 0
dataSentCounter = 0

while dataSentCounter < numberOfPackages:
    EB = random.randrange(0,16)
    #EB = 5 #For testing purposes
    EB_History.append(EB)
    print("EB elegido:",EB)
    for eb in range(EB,-1,-1):
        print("Tiempo",time,"(",timer,")","Esperando... EB =",eb)
        time = time + 1
        timer = timer + DIFS
    timer = timer - DIFS # Adjustment, EB = 0 at the same time data is sent
    print("Tiempo",time,"(",timer,")","Inicia envío de paquete de datos...")
    timer = timer + dataSendTime
    time = time + 1
    print("Tiempo",time,"(",timer,")","Inicia espera de acknowledge...")
    timer = timer + SIFS
    time = time + 1
    print("Tiempo",time,"(",timer,")","Inicia recepción de acknowledge...")
    timer = timer + ackSendTime
    time = time + 1
    dataSentCounter = dataSentCounter + 1

print("Promedio del Exponential Backup:",sum(EB_History)/len(EB_History))
print("Tiempo total de transmisión de",numberOfPackages,"paquetes:",timer,"segundos")
print("Throughput:",((numberOfPackages * data * 8)/timer)/1000,"Kbps")