#correos

import smtplib

destinatario="benjamin.wwe@hotmail.es"
remitente="pythonIsCool2017@gmail.com"
password="python123"

smtpServer=smtplib.SMTP("smtp.gmail.com",587)

smtpServer.ehlo()

smtpServer.starttls()

smtpServer.ehlo()

smtpServer.login(remitente,password)

header="De:"+remitente+" Para: "+destinatario+"\n"+"Subject: Prueba smtplib\n"
print(header)

mensaje=header+'\n esto debe aparecer en el cuerpo de correo \n\n'

smtpServer.sendmail(remitente,destinatario,mensaje)

print("Enviado!")

smtpServer.close()
