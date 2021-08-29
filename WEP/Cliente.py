import socket
import crcmod.predefined

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Puertos
socket_client.connect(("localhost",9999))
received = socket_client.recv(1024)
received = received.decode('utf-8')
print("Lo que recibimos del servidor:",received)

# Iniciamos WEP
SboxSize = 8
WEPkey = "12345"
respuesta = "Hola server!"
newInicializationVector = "A21"
crc32_func = crcmod.predefined.mkCrcFun('crc-32') # Genera funcion CRC32

# Obtenemos el vector de inicializacion enviado por el servidor
InicializationVector = received[0:3]

# Creamos la misma semilla que el servidor
semilla = InicializationVector + WEPkey

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

    # Ahora vamos a responder el mensaje con un nuevo vector de inicializacion

    # Creamos la nueva semilla
    semilla = newInicializationVector + WEPkey

    # Generamos la nueva S-box
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

    # Concatenamos la respuesta con el CRC-32
    respuestaNumeros = ""
    for i in respuesta:
        respuestaNumeros = respuestaNumeros + str(ord(i))
    respuestaCRC = respuestaNumeros + str(crc32_func(bytes(respuestaNumeros,'utf-8')))

    # Hacemos el XOR de la Key Sequence y la respuestaCRC
    Ciphertext = int(keySequence) ^ int(respuestaCRC)

    # Envia la respuesta cifrada
    print("respuesta enviada:",newInicializationVector + str(Ciphertext))
    socket_client.send(bytes(newInicializationVector + str(Ciphertext),'utf-8'))

    # Cerramos
    socket_client.close()
else:
    print("El mensaje recibido fue corrompido")

# Cerramos
    socket_client.close()
