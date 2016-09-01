#####Ejemplo diccionario "agenda"#####

'''Comentario de más 
una sola 
linea
'''

agenda={ "alan":["551338760423","alan@proteco.mx",22,True],
		 "luis":[456304785034,"correo",15],	
         "laura":["234234","otrocorreo",16]  
}

#Se busca con la llave para obtener el valor
nombre=input("A quien deseas buscar?:")
print("El numero de "+nombre+" es:",agenda[nombre][0])