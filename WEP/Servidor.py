import socket
import crcmod.predefined

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Definiendo puertos:
socket_server.bind(("25.92.219.0",9999))
#socket_server.bind(("localhost",9999))
# Cuantos hosts se van a comunicar con el servidor
socket_server.listen(1) # Esta función también pone al servidor en modo de escucha, esperando una petición
# Aceptando la petición. Se crea el cliente
socket_client, (remote_client_ip, remote_client_tcp) = socket_server.accept()
print ("ip client: ", remote_client_ip)
print ("tcp client: ", remote_client_tcp)

# Comenzamos con WEP
SboxSize = 8
WEPkey = "12345"
InicializationVector = "123"
mensaje = "hola"
crc32_func = crcmod.predefined.mkCrcFun('crc-32') # Genera funcion CRC32

# Creamos la semilla
semilla = InicializationVector + WEPkey
print("semilla:",semilla)

# Generamos la S-box
Sbox = list(range(SboxSize)) # Llenamos la S-box
Kbox = list(range(SboxSize))
for i in range(SboxSize):
    Kbox[i] = ord(list(semilla)[i % len(semilla)]) # Llenamos la K-box
j = 0
for i in range(SboxSize): # Generamos la S-box
    j = (j + Sbox[i] + Kbox[i]) % SboxSize
    intermedia = Sbox[i]
    Sbox[i] = Sbox[j]
    Sbox[j] = intermedia
print("Sbox antes de RC4:",Sbox)

# Hacemos RC4
j = 0
for i in range(SboxSize):
    i = (i + 1) % SboxSize
    j = (j + Sbox[i]) % SboxSize
    intermedia = Sbox[i]
    Sbox[i] = Sbox[j]
    Sbox[j] = intermedia
    t = (Sbox[i] + Sbox[j]) % SboxSize
    Kbox[i] = Sbox[t]
keySequence = ''.join(str(a) for a in Kbox) # Volvemos la lista de la K-box una cadena
print("Key Sequence:",keySequence)

# Concatenamos el mensaje con el CRC-32
mensajeNumeros = ""
for i in mensaje:
    mensajeNumeros = mensajeNumeros + str(ord(i))
mensajeCRC = mensajeNumeros + str(crc32_func(bytes(mensajeNumeros,'utf-8')))
print("Mensaje en numeros:",mensajeNumeros)
print("Mensaje en numeros concatenado con CRC:",mensajeCRC)

# Hacemos el XOR de la Key Sequence y el mensajeCRC
Ciphertext = int(keySequence) ^ int(mensajeCRC)
#print("Ciphertext:",Ciphertext)
#print("Key Sequence:",keySequence)

# Envia el mensaje cifrado
InicializationVector = "A23" # Metemos un error en el envio del mensaje
print("mensaje enviado:",InicializationVector + str(Ciphertext))
socket_client.send(bytes(InicializationVector + str(Ciphertext),'utf-8'))

# Espera a recibir respuesta
received = socket_client.recv(1024)
received = received.decode('utf-8')
print("respuesta recibida del cliente:",received)

# Obtenemos el vector de inicializacion enviado por el servidor
newInicializationVector = received[0:3]

# Creamos la misma semilla que el servidor
semilla = newInicializationVector + WEPkey

# Generamos la misma S-box que el servidor
Sbox = list(range(SboxSize)) # Llenamos la S-box
Kbox = list(range(SboxSize))
for i in range(SboxSize):
    Kbox[i] = ord(list(semilla)[i % len(semilla)]) # Llenamos la K-box
j = 0
for i in range(SboxSize): # Generamos la S-box
    j = (j + Sbox[i] + Kbox[i]) % SboxSize
    intermedia = Sbox[i]
    Sbox[i] = Sbox[j]
    Sbox[j] = intermedia

# Hacemos RC4 para generar la misma Key Sequence que el servidor
j = 0
for i in range(SboxSize):
    i = (i + 1) % SboxSize
    j = (j + Sbox[i]) % SboxSize
    intermedia = Sbox[i]
    Sbox[i] = Sbox[j]
    Sbox[j] = intermedia
    t = (Sbox[i] + Sbox[j]) % SboxSize
    Kbox[i] = Sbox[t]
keySequence = ''.join(str(a) for a in Kbox) # Volvemos la lista de la K-box una cadena
#print("Key Sequence:",keySequence)

# Hacemos el XOR de la Key Sequence y el mensaje cifrado recibido
mensajeCRC = int(keySequence) ^ int(received[3:])
#print("Key Sequence:",keySequence)
#print("Ciphertext:",received[3:])
#print("Mensaje en numeros concatenado con CRC:",mensajeCRC)

# Separamos mensaje de CRC
mensaje = str(mensajeCRC)[0:len(str(mensajeCRC))-10]
ElCRC = str(mensajeCRC)[-10:]

# Revisamos la integridad del mensaje
if ElCRC == str(crc32_func(bytes(mensaje,'utf-8'))):
    print("Integridad del mensaje recibido verificada!")
    # Obtenemos el mensaje en texto plano
    textoPlano = ""
    i = 0
    while i < len(mensaje):
        if int(mensaje[i:i+2]) > 31 and int(mensaje[i:i+2]) < 123:
            textoPlano = textoPlano + chr(int(mensaje[i:i+2]))
            i = i + 2
        else:
            textoPlano = textoPlano + chr(int(mensaje[i:i+3]))
            i = i + 3
    #print("Mensaje en numeros:",mensaje)
    print("Mensaje recibido en texto plano:",textoPlano)

    socket_client.close()
    socket_server.close()
else:
    print("El mensaje recibido fue corrompido")