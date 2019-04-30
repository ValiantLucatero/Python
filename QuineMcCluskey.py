def mul(x, y):  # Multiplica 2 minterminos
    res = []
    for i in x:
        if i+"'" in y or (len(i)==2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res

def multiply(x,y): # Multiplica 2 expresiones
    res = []
    for i in x:
        for j in y:
            tmp = mul(i,j)
            res.append(tmp) if len(tmp) != 0 else None
    return res

def refine(my_list,dc_list): # Remueve terminos don´t care de una lista dada y regresa la lista refinada
    res = []
    for i in my_list:
        if int(i) not in dc_list:
            res.append(i)
    return res

def findEPI(x): # Función para encontrar los implicantes primos esenciales de la tabla de implicantes primos
    res = []
    for i in x:
        if len(x[i]) == 1:
            res.append(x[i][0]) if x[i][0] not in res else None
    return res

def findVariables(x): # Función para encontrar variables en un mintermino. Por ejemplo, el mintermino --01 tiene C' y D como variables
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i+65)+"'")
        elif x[i] == '1':
            var_list.append(chr(i+65))
    return var_list

def flatten(x): # Aplana una lista
    flattened_items = []
    for i in x:
        flattened_items.extend(x[i])
    return flattened_items

def findminterms(a): # Función para encontrar que minterminos estan unidos. Por ejemplo, 10-1 se obtiene uniendo 9(1001) y 11(1011)
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

def compare(a,b): # Función para checar si 2 minterminos difieren en solo 1 bit
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_index = i
            c += 1
            if c>1:
                return (False,None)
    return (True,mismatch_index)

def removeTerms(_chart,terms): # Remueve minterminos que ya estan cubiertos en la tabla
    for i in terms:
        for j in findminterms(i):
            try:
                del _chart[j]
            except KeyError:
                pass

mt = [int(i) for i in input("Ingresa los minterminos: ").strip().split()]
dc = [int(i) for i in input("Ingresa los don't cares(si hay): ").strip().split()]
mt.sort()
minterms = mt+dc
minterms.sort()
size = len(bin(minterms[-1]))-2
groups,all_pi = {},set()

# Comienza la agrupación primaria
for minterm in minterms:
    try:
        groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
    except KeyError:
        groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
# Termina la agrupación primaria

# Inicia la impresión del grupo primario
print("\n\n\n\nGrupo No. \tMinterminos\tBinario de Minterminos\n%s"%('='*50))
for i in sorted(groups.keys()):
    print("%5d:"%i) # Imprime el número de grupo
    for j in groups[i]:
        print("\t\t           %-20d%s"%(int(j,2),j)) # Imprime el mintermino y su representación en binario
    print('-'*50)
# Termina la impresión del grupo primario

# Inicia el proceso del creado de tablas y busqueda de los implicantes primos
while True:
    tmp = groups.copy()
    groups,m,marked,should_stop = {},0,set(),True
    l = sorted(list(tmp.keys()))
    for i in range(len(l)-1):
        for j in tmp[l[i]]: # Ciclo que itera a través de los elementos del grupo actual
            for k in tmp[l[i+1]]: # Ciclo que itera a través de los elementos del siguiente grupo
                res = compare(j,k) # Compara los minterminos
                if res[0]: # Si los minterminos difieren en solo 1 bit
                    try:
                        groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None # Pone un '-' en el bit cambiante y lo agrega al grupo correspondiente
                    except KeyError:
                        groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] # Si el grupo no existe, crea el grupo primero y luego pone un '-' en el bit cambiante y lo agrega al nuevo grupo creado
                    should_stop = False
                    marked.add(j) # Marca el elemento j
                    marked.add(k) # Marca el elemento k
        m += 1
    local_unmarked = set(flatten(tmp)).difference(marked) # Desmarca los elementos de cada tabla
    all_pi = all_pi.union(local_unmarked) # Agregando los implicantes primos a la lista global
    print("Elementos no marcados(Implicantes Primos) de esta tabla:",None if len(local_unmarked)==0 else ', '.join(local_unmarked)) # Imprime los implicantes primos de la tabla actual
    if should_stop: # Si los minterminos ya no se pueden combinar
        print("\n\nTodos los Implicantes Primos: ",None if len(all_pi)==0 else ', '.join(all_pi)) # Imprime todos los implicantes primos
        break
    # Inicia la impresión de todos los grupos siguientes
    print("\n\n\n\nGrupo No. \tMinterminos\tBinario de Minterminos\n%s"%('='*50))
    for i in sorted(groups.keys()):
        print("%5d:"%i) # Imprime el número de grupo
        for j in groups[i]:
            print("\t\t       %-24s%s"%(','.join(findminterms(j)),j)) # Imprime los minterminos y su representación en binario
        print('-'*50)
    # Termina la impresión de todos los siguientes grupos
# Termina el proceso de creación de tablas y de encontrar implicantes primos


# Inicia la impresión y procesamiento de la tabla de implicantes primos
sz = len(str(mt[-1])) # El número de dígitos del mintermino más grande
chart = {}
print('\n\n\nTabla de Implicantes Primos:\n\n   Mintérminos  |%s\n%s'%(' '.join((' '*(sz-len(str(i))))+str(i) for i in mt),'='*(len(mt)*(sz+1)+16)))
for i in all_pi:
    merged_minterms,y = findminterms(i),0
    print("%-16s|"%','.join(merged_minterms),end='')
    for j in refine(merged_minterms,dc):
        x = mt.index(int(j))*(sz+1) # La posición donde debo poner 'X'
        print(' '*abs(x-y)+' '*(sz-1)+'X',end='')
        y = x+sz
        try:
            chart[j].append(i) if i not in chart[j] else None # Agrega el mintermino a la tabla
        except KeyError:
            chart[j] = [i]
    print('\n'+'-'*(len(mt)*(sz+1)+16))
# Termina la impresión y procesamiento de la tabla de implicantes primos

EPI = findEPI(chart) # Encuentra los implicantes primos esenciales
print("\nImplicantes Primos Esenciales: "+', '.join(str(i) for i in EPI))
removeTerms(chart,EPI) # Remueve las columnas relacionadas con los EPI de la tabla

if(len(chart) == 0): # Si no quedan minterminos después de quitar las columnas relacionadas con los EPI
    final_result = [findVariables(i) for i in EPI] # Resultado final solo con EPIs
else: # Si no, seguimos el método de Petrick para simplificar más
    P = [[findVariables(j) for j in chart[i]] for i in chart]
    while len(P)>1: # Sigue multiplicando hasta que obtengamos la SOP de P
        P[1] = multiply(P[0],P[1])
        P.pop(0)
    final_result = [min(P[0],key=len)] # Eligiendo el término con menos variables de P
    final_result.extend(findVariables(i) for i in EPI) # Sumando los EPIs a la solución final
print('\n\nSolución: F = '+' + '.join(''.join(i) for i in final_result))

input("\nPresiona enter para salir...")
