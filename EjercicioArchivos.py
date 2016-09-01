lineas = [linea.rstrip('\n') for linea in open("texto.txt")]
print(lineas[:len(lineas)//2])