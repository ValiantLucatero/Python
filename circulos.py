##########
# Circulos
##########

#importamos un módulo que tiene funciones y constantes matemáticas
import math


radio=float(input("Dame el radio: "))

perimetro=2*math.pi*radio
area=radio*radio*math.pi
volumen=(4/3)*math.pi*radio**3

#Usamos los especificadores de formato
print("El perimetro si fuera circunferencia: %.3f" %(perimetro))
print("El area si fuera círculo es: %.3f"%(area))
print("El volumen si fuera esfera es: %.3f"%(volumen))