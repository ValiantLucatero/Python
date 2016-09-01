######
# MAGICOS
######

#Son metodos que se mandan a llamar cuando queremos que los objetos se comporten de cierta manera

class Coordenada:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	#add se manda a llamar cuando se quieren sumar dos objetospor medio del operador +
	#devolvemos un nuevo objeto de la misma clase
	def __add__(self,otro):
		"""Cuando sumamos una Coordenada con otra"""
		return Coordenada(self.x+otro.x,self.y+otro.y)

	## se pueden sobreescribir todos operadores aritmeticos
	## __sub__ -> resta
	## __mul__ -> multiplicacion
	## __div__ -> division
	## __pow__ -> potencia 
	## __mod__ -> modulo

	def __str__(self):
		"""Cuando imprimimos una coordenada"""
		return "(%d,%d)"%(self.x,self.y)

	def __getitem__(self,indice):
		"""Cuando mandamos a llamar una coordenada como si fuera lista"""
		if indice==0:
			return self.x
		else:
			return self.y

c1=Coordenada(5,6)
c2=Coordenada(7,4)
c3 = c1+c2
#c4 = c1+"Hola"
print(c3.x,",",c3.y)
print(c3)
print(c1)
print(c2)
print(c1[0])
c1[0]=5
