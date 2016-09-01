#Casteos#

#Casteo: convertir de un tipo de dato a otro

#intput lo toma directamente como cadena
num=input("Dame un numero:")
num=3
#aqui lo convertimos a entero con la funcion int()
res=int(num)*3


#Podemos volver a castearlo para imprimirlo todo como cadena
print("Tu numero: "+str(res))
#O simplemente lo separamos con comas
#print("Tu numero: ",res)

#Para checar tipos de datos tenemos la funcion type()
print(type(num))

#Para castear de lista a cadena se usa la funcion join

lista1 = ['1', '2', '3']
print(type(lista1))

str1 = ''.join(lista1)
print(type(str1))

