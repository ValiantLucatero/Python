import bisect

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
a = input("Dame el numero del elemento que buscas: ")
i = 1
print("Buscando {} en numeros:".format(a))

# Método común: iteramos sobre la tupla elemento por elemento
for numero in numeros:
    if numero == a:
        print("Por el método largo lo encontré en {} iteraciones".format(i))
    else:
        i += 1


# Método divide y vencerás
def divideYvenceras(lista, a):
    j = 0
    inicio = 0
    fin = len(lista) - 1
    while True:
        if fin < inicio:
            respuesta = "Ese elemento no esta en la lista"
            return respuesta
        mitad = (inicio + fin) // 2
        if lista[mitad] < a:
            j += 1
            inicio = mitad + 1
        elif lista[mitad] > a:
            j += 1
            fin = mitad - 1
        else:
            respuesta = "Por Divide y Vencerás en {} iteraciones".format(j)
            return respuesta


print(divideYvenceras(numeros, a))

# devuelve el lugar donde se encuentra el elemento
# si no lo encuentra te dice cual es el elemento mas cercano
print(bisect.bisect_left(numeros, a))
