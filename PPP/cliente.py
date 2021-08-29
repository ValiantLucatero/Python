import socket
import crcmod.predefined
# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Puertos
socket_client.connect(("localhost",9999))
received = socket_client.recv(1024)
received = received.decode('utf-8')
print("Lo que recibimos del servidor:",received)

# Iniciamos PPP
password = "porFavorProfe10"
escape = "01111101"
flag = "01111110"

# Obtenemos el Challenge enviado por el servidor
# Hacemos el unstuffing
unstuffed = (received.replace(escape+escape, escape)).replace(escape+flag,flag)

# Obtenemos la longitud en binario
serverChallengeSize = unstuffed[40+8+8+16:40+8+8+16+8]

# La pasamos a decimal
serverChallengeSizeDecimal = int(serverChallengeSize,2)

#print("Longitud del challenge en decimal:",serverChallengeSizeDecimal)

# Obtenemos la cadena del challenge
serverChallenge = unstuffed[40+8+8+16+8:40+8+8+16+8+serverChallengeSizeDecimal]

crc16_func = crcmod.predefined.mkCrcFun('crc-16') # Genera funcion CRC16

# Opera el challenge con la contra
check = serverChallenge + password
compare = bin(crc16_func(bytes(check,'utf-8'))).replace("0b","")
#print("CRC-16 de challenge y password:",compare)

# Construimos payload del response message
responseValue = compare # Valor calculado con CRC-16, password y challenge recibido
responseName = (''.join(format(ord(x), '08b') for x in "RE")) # Name = CH, RE
responseLength = bin(len(responseValue)).replace("0b", "") #longitud del response
while len(responseLength) < 8: # Agrega 0s al inicio para que sea de 16 bits siempre
    responseLength = "0"+responseLength
length = bin(8+8+16+len(responseValue)+len(responseName)+len(responseLength)).replace("0b", "") #longitud del payload
while len(length) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
    length = "0"+length
response = "00000010"+"00000001"+length+responseLength+responseValue+responseName #Armamos el sub-bloque completo del response
#print("response String:",responseValue)
#print("tamanio del response string en binario:",responseLength)
#print("response payload completo:",response)

# Construimos el response message
address = "11111111"
control = "00000011"
protocol = bin(int("C223", 16)).replace("0b", "") # Protocol = 0xC223 = 1100001000100011
preHeader = address + control + protocol # PreHeader constante de 40
payload =  response #Response que enviará
fcs = bin(crc16_func(bytes(address+control+protocol+payload,'utf-8'))).replace("0b","") #Genera el FCS con CRC16 al address, control, protocol y payload
while len(fcs) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
    fcs = "0"+fcs

message = preHeader+payload+fcs
#print("mensaje antes del stuffing:",message)

# Hace el byte-stuffing del mensaje:
stuffed = (message.replace(escape, escape+escape)).replace(flag,escape+flag)

#Ponemos banderas
stuffed = flag+stuffed+flag

# Envia response
print("mensaje con response enviado:",stuffed)
socket_client.send(bytes(stuffed,'utf-8'))

# Espera a recibir respuesta
received = socket_client.recv(1024)
received = received.decode('utf-8')
print("mensaje recibido del servidor:",received)

# Revisamos si fue un Ack o un Nack
# Hacemos el unstuffing
unstuffed = (received.replace(escape+escape, escape)).replace(escape+flag,flag)

# Obtenemos la respuesta
serverResponse = unstuffed[40+8+8+16:40+8+8+16+8]
print("Respuesta del servidor:",serverResponse)

#Revisamos
if serverResponse == "11111111":
    # Enviamos mensaje
    payload = (''.join(format(ord(x), '08b') for x in "Hola! Me puedes leer?")) #Mensaje que enviará
    #print("Mensaje en binario:",payload)
    fcs = bin(crc16_func(bytes(address+control+protocol+payload,'utf-8'))).replace("0b","") #Genera el FCS con CRC16 al address, control, protocol y payload
    while len(fcs) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
        fcs = "0"+fcs

    message = preHeader+payload+fcs

    # Hace el byte-stuffing del mensaje:
    stuffed = (message.replace(escape, escape+escape)).replace(flag,escape+flag)

    #Ponemos banderas
    stuffed = flag+stuffed+flag

    # Envia mensaje
    print("mensaje enviado:",stuffed)
    socket_client.send(bytes(stuffed,'utf-8'))

    # Cerramos
    socket_client.close()

else:
    # Cerramos
    socket_client.close()
