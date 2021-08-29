import socket
import crcmod.predefined
# un socket = (dir IP, dir TCP)
# creando un socket: que protocolos
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Definiendo puertos:
socket_server.bind(("25.92.219.0", 9999))
# Cuantos hosts se van a comunicar con el servidor
socket_server.listen(1) # Esta función también pone al servidor en modo de escucha, esperando una petición
# Aceptando la petición. Se crea el cliente
socket_client, (remote_client_ip, remote_client_tcp) = socket_server.accept()
print ("ip client: ", remote_client_ip)
print ("tcp client: ", remote_client_tcp)

# Comenzamos con PPP
crc16_func = crcmod.predefined.mkCrcFun('crc-16') # Genera funcion CRC16

# Construimos payload del challenge message
challengeValue = (''.join(format(ord(x), '08b') for x in "Poganos10Profe")) # Valor del String de Challenge
challengeName = (''.join(format(ord(x), '08b') for x in "CH")) # Name = CH, RE
challengeLength = bin(len(challengeValue)).replace("0b", "") #longitud del challenge
while len(challengeLength) < 8: # Agrega 0s al inicio para que sea de 16 bits siempre
    challengeLength = "0"+challengeLength
length = bin(8+8+16+len(challengeValue)+len(challengeName)+len(challengeLength)).replace("0b", "") #longitud del payload
while len(length) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
    length = "0"+length
challenge = "00000001"+"00000001"+length+challengeLength+challengeValue+challengeName #Armamos el sub-bloque completo del challenge
#print("challenge String:",challengeValue)
#print("tamanio del challenge string en binario:",challengeLength)
#print("challenge completo:",challenge)

# Construimos el challenge message
password = "porFavorProfe10"
escape = "01111101"
flag = "01111110"
address = "11111111"
control = "00000011"
protocol = bin(int("C223", 16)).replace("0b", "") # Protocol = 0xC223 = 1100001000100011
preHeader = address + control + protocol # PreHeader constante de 40
payload = challenge #Challenge que enviará
fcs = bin(crc16_func(bytes(address+control+protocol+payload,'utf-8'))).replace("0b","") #Genera el FCS con CRC16 al address, control, protocol y payload
while len(fcs) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
    fcs = "0"+fcs
message = preHeader+payload+fcs
#print("mensaje con challenge:",message)

# Hace el byte-stuffing del mensaje:
stuffed = (message.replace(escape, escape+escape)).replace(flag,escape+flag)

#Ponemos banderas
stuffed = flag+stuffed+flag

# Envia challenge
print("mensaje enviado con bytestuffing:",stuffed)
socket_client.send(bytes(stuffed,'utf-8'))

# Opera el challenge con la contra
check = challengeValue + password
compare = bin(crc16_func(bytes(check,'utf-8'))).replace("0b","")
#print("CRC-16 de challenge y password:",compare)

# Espera a recibir respuesta
received = socket_client.recv(1024)
received = received.decode('utf-8')
print("response recibido del cliente:",received)

# Hace el unstuffing
unstuffed = (received.replace(escape+escape, escape)).replace(escape+flag,flag)
#print("response unstuffed:",unstuffed)

# Obtiene el challenge calculado por el cliente
clientChallenge = unstuffed[40+8+8+16+8:40+8+8+16+8+len(compare)]
#print("Challenge calculado por el cliente:",clientChallenge)

# Compara lo recibido con lo calculado
if clientChallenge == compare:
    # Construimos payload del acknowledge message
    acknowledgeMessage = "11111111"
    length = bin(8+8+16+8).replace("0b", "") #longitud del payload
    while len(length) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
        length = "0"+length
    payload = "00000011"+"00000001"+length+acknowledgeMessage #Armamos el sub-bloque completo del acknowledge
    #print("tamanio del acknowledge message en binario:",length)
    #print("acknowledge completo:",payload)
    fcs = bin(crc16_func(bytes(address+control+protocol+payload,'utf-8'))).replace("0b","") #Genera el FCS con CRC16 al address, control, protocol y payload
    while len(fcs) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
        fcs = "0"+fcs
    acknowledge = preHeader+payload+fcs

    # Hace el byte-stuffing del acknowledge:
    stuffed = (acknowledge.replace(escape, escape+escape)).replace(flag,escape+flag)

    #Ponemos banderas
    stuffed = flag+stuffed+flag

    # Envia acknowledge
    socket_client.send(bytes(stuffed,'utf-8'))
    print("acknowledge enviado con bytestuffing:",stuffed)

    # Espera el mensaje del cliente
    received = socket_client.recv(1024)
    received = received.decode('utf-8')
    print("Mensaje recibido del cliente",received)

    # Aplica el bitUnstuffing
    unstuffed = (received.replace(escape+escape, escape)).replace(escape+flag,flag)

    # Extrae el mensaje
    clientMessage = unstuffed[40:-24]
    #print("Mensaje recibido en binario:",clientMessage)

    #String vacio para ir almacenando los caracteres
    str_data = ''
   
    # Cortamos cada 8 caracteres para hacer un byte, luego transformarlo a int y luego a string
    for i in range(0, len(clientMessage), 8):
      
        # vamos almacenando lo cortado en temp_data
        temp_data = clientMessage[i:i + 8]
       
        # obtenemos el valor decimal para el binario recortado
        decimal_data = int(temp_data, 2)
       
        # Transformamos a caracter usando la funcion chr() que nos regresa un valor ASCII por cada caracter
        str_data = str_data + chr(decimal_data)
        #print("caracter",chr(decimal_data))
  
    # Imprimimos el resultado
    print("Mensaje recibido del cliente:")
    print(str_data)

    #Cerramos conexion
    socket_client.close()
    socket_server.close()

else:
    # Construimos payload del Nacknowledge message
    NacknowledgeMessage = "00000000"
    length = bin(8+8+16+8).replace("0b", "") #longitud del payload
    while len(length) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
        length = "0"+length
    payload = "00000100"+"00000001"+length+NacknowledgeMessage #Armamos el sub-bloque completo del Nacknowledge
    #print("tamanio del Nacknowledge message en binario:",length)
    #print("Nacknowledge completo:",payload)
    fcs = bin(crc16_func(bytes(address+control+protocol+payload,'utf-8'))).replace("0b","") #Genera el FCS con CRC16 al address, control, protocol y payload
    while len(fcs) < 16: # Agrega 0s al inicio para que sea de 16 bits siempre
        fcs = "0"+fcs
    Nacknowledge = preHeader+payload+fcs

    # Hace el byte-stuffing del Nacknowledge:
    stuffed = (Nacknowledge.replace(escape, escape+escape)).replace(flag,escape+flag)

    #Ponemos banderas
    stuffed = flag+stuffed+flag

    # Envia NoAcknowledge
    socket_client.send(bytes(stuffed,'utf-8'))
    print("Nacknowledge enviado con bytestuffing:",stuffed)

    socket_client.close()
    socket_server.close()