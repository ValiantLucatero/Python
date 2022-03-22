num = int(input("Ingresa un número:"))
for i in range(2,num):
    if num%i == 0:
        print("No es primo")
        exit()
print("Es primo")