#Gráfica de la función
plt.figure(1)
x = np.linspace(a,b,101)
plt.plot(x,f(x),label="$f(x)$")
plt.plot(x,0*x,label="Eje x")
plt.title("Falsa Posicion")
plt.grid(True)
plt.legend()

#Método
maxIter=100 #Número máximo de iteraciones
epsilon=1*10**(-8) #Margen de error

for i in range(maxIter):
    #Checar presentacion
        
print(f"La raíz aproximada es xm = {xm} y se obtuvo con {i+1} iteraciones")
plt.show()
