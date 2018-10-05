"""Reto 2."""
import re
f = open("config_demo.txt", "r")
f.seek(0)
cadena = f.read()
f.close()
noSerie = re.compile("SN: (.+)")
result1 = noSerie.search(cadena)
modelo = re.compile("DESCR: (.+)")
result2 = modelo.search(cadena)
MAC = re.compile("MAC Address\.+ (.+)")
result3 = MAC.search(cadena)
softVer = re.compile("Product Version\.+ (.+)")
result4 = softVer.search(cadena)
upTime = re.compile("System Up Time\.+ (.+)")
result5 = upTime.search(cadena)
sysLoc = re.compile("System Location\.+ (.+)")
result6 = sysLoc.search(cadena)
ipMan = re.compile("IP Address\.+ (.+)")
result7 = ipMan.search(cadena)
diccionario = {
    "No serie": result1.group(1),
    "Modelo": result2.group(1),
    "MAC": result3.group(1),
    "Version de soft": result4.group(1),
    "uptime": result5.group(1),
    "ubicacion del sistema": result6.group(1),
    "IP management": result7.group(1)
}
print(diccionario)
