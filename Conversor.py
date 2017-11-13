x = input("Hola usuario selecciona la opcion que quieras realizar:\n1)Transformar de sistema metrico a ingles\n2)Transformar de sistema ingles a metrico\n")
if x == 1:
  #Metrico a Ingles
  n=int(input("Ingresa el dato a convertir en metros: "))#recibe el dato y lo castea a int para hacer operaciones
  pulgada=n*39.3701
  pie=n*3.28084       #factores de conversion
  yarda=n*1.09361
  milla=n*0.000621371
  print "{} metros son: {} pulgadas, {} pies, {} yardas y {} millas" .format(n, pulgada, pie, yarda, milla)
elif x == 2:
    #Ingles a Metrico
    n=int(input("Ingresa el dato a convertir: "))
    u=input("Selecciona en que unidad se encuentra:\n1)pulgada\n2)pie\n3)yarda\n4)milla\n")
    if u == 1:
        metro=n*0.0254
        milimetro=n*25.4
        centimetro=n*2.54
        kilometro=n*0.0000254
        print "{} pulgadas son: {} milimetros, {} centimetros, {} metros y {} kilometros" .format(n, milimetro, centimetro, metro, kilometro)
    elif u == 2:
        metro=n*0.3048
        milimetro=n*304.8
        centimetro=n*30.48
        kilometro=n*0.0003048
        print "{} pies son: {} milimetros, {} centimetros, {} metros y {} kilometros" .format(n, milimetro, centimetro, metro, kilometro)
    elif u == 3:
        metro=n*0.9144
        milimetro=n*914.4
        centimetro=n*91.44
        kilometro=n*0.0009144
        print "{} yardas son: {} milimetros, {} centimetros, {} metros y {} kilometros" .format(n, milimetro, centimetro, metro, kilometro)
    elif u == 4:
        metro=n*1609.34
        milimetro=n*1609000
        centimetro=n*160934
        kilometro=n*1.60934
        print "{} millas son: {} milimetros, {} centimetros, {} metros y {} kilometros" .format(n, milimetro, centimetro, metro, kilometro)
    else:
        print("Ingresa una opcion valida")
else:
    print("Ingresa una opcion valida")
