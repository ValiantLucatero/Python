print("Ejemplo de tipado:")

#a y b son enteros
a=5
b=4
#su suma obiamente es un entero
c=a+b

#no importan los espacios que dejen dentro de las funciones
#solo los que son antes
print("a:",a," b:",    b   , " c:",c)

a=b #referenciamos ... ahora a apunta a lo que hay en b a -> b ->4
a+=1 #lo mismo que a++ en otros lenguajes a=4+1
c=b+a # =9


print("a:",a," b:",    b   , " c:",c)
