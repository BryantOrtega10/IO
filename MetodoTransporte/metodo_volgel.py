#Autor: Bryant Ortega
#Fecha creación: 01/03/2022
#Se crea una clase celda que contendra los costos, la demanda aplicada a esa celda y el estado (Tachado o no)
class celda:
    def __init__(self, costo, demanda = 0, estado = True):
        self.costo = costo
        self.demanda = demanda
        self.estado = estado

#Cambia el estado de una fila en la matriz de costos
def cambiarEstadoFila(fila, tabla):
    for i in range(len(tabla)):
        if(i == fila):
            for j in range(len(tabla[i])):
                tabla[i][j].estado = False
            
#Cambia el estado de una columna en la matriz de costos
def cambiarEstadoColumna(col, tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if(j == col):
                tabla[i][j].estado = False

#Verifica si todas las demandas y ofertas han sido cumplidas
def demandas_ofertas_0(demanda, oferta):
    for d in demanda:
        if d!=0:
            return False
    for o in oferta:
        if o!=0:
            return False
    return True

#busca los costes minimos en una fila y los resta
def buscarMinimosCostesFila(tabla,fila):
    aux = []
    for j in range(len(tabla[fila])):
        if  tabla[fila][j].estado:
            aux.append(tabla[fila][j].costo)
    aux.sort()
    
    if(len(aux)>=2):
        return aux[1]-aux[0]
    elif len(aux)==1:
        return aux[0]
    else:
        return 0

#busca los costes minimos en una columna y los resta
def buscarMinimosCostesColumna(tabla,col):
    aux = []
    for i in range(len(tabla)):
        if  tabla[i][col].estado:
            aux.append(tabla[i][col].costo)
    aux.sort()
    
    if(len(aux)>=2):
        return aux[1]-aux[0]
    elif len(aux)==1:
        return aux[0]
    else:
        return 0

#Busca en la matriz de penalizacion la penalizacion mas grande y devuelve sus coordenadas
def buscarMaximaPenalizacion(penalizacion):
    aux = None
    pos = (0,0)
    for i in range(len(penalizacion)):
        for j in range(len(penalizacion[i])):
            if aux is None or aux < penalizacion[i][j]:
                aux = penalizacion[i][j]
                pos = (i,j)
    return pos

#Busca en la matriz de costos el costo minimo en la fila
def buscarDispEnFila(tabla, fila):
    aux = None
    for j in range(len(tabla[fila])):
        if (aux is None or aux > tabla[fila][j].costo) and tabla[fila][j].estado:
            aux = j
    return aux

#Busca en la matriz de costos el costo minimo en la columna
def buscarDispEnCol(tabla, col):
    aux = None
    for i in range(len(tabla)):
        if (aux is None or aux > tabla[i][col].costo) and tabla[i][col].estado:
            aux = i
    return aux

#Se crea la matriz de objetos tipo celda
tabla = [
    [celda(10),celda(2),celda(20),celda(11)],
    [celda(12),celda(7),celda(9),celda(20)],
    [celda(4),celda(14),celda(16),celda(18)]
]

#Se crea el arreglo de demanda el primer elemento es el de mas a la izquierda
demanda = [5,15,15,15]
#Se crea el arreglo de oferta el primer elemento es el de mas arriba
oferta = [15,25,10]


#Se verifica si todas las demandas o las ofertas estan en 0, si no se cumple esa condicion entra al ciclo
while not demandas_ofertas_0(demanda, oferta):
    #Crea/Reinicia las penalizaciones
    penalizacion = [[],[]]
    #Asigna las penalizaciones de las filas
    for i in range(len(tabla)):
        penalizacion[0].append(buscarMinimosCostesFila(tabla,i))
    #Asigna las penalizaciones de las columnas
    for j in range(len(tabla[0])):
        penalizacion[1].append(buscarMinimosCostesColumna(tabla,j))
    #Asigna a las variables i,j las posiciones de la mayor penalizacion
    i,j = buscarMaximaPenalizacion(penalizacion)
    #Si la primera variable es 0, significa que la penalizacion esta en una fila
    if i == 0:
        #Se asigna a x el valor de j, para indicar que esta en esa fila el elemento que deseamos
        x = j
        #Se busca en la matriz costos, el minimo costo en esa fila
        y = buscarDispEnFila(tabla, x)
    else:
        #Se asigna a y el valor de j, para indicar que esta en esa columna el elemento que deseamos
        y = j
        #Se busca en la matriz costos, el minimo costo en esa colimna
        x = buscarDispEnCol(tabla, y)

    #Verifica si es mayor la oferta o la demanda en esa coordenada
    if oferta[x] > demanda[y]:
        #En caso de mayor oferta resto a la oferta el total de la demanda
        oferta[x] = oferta[x] - demanda[y]
        #Se asigna a la matriz de costos la demanda correspondiente para esa celda
        tabla[x][y].demanda = demanda[y]
        #Como la demanda ya fue asignada se cambia la demanda en esa posicion a 0
        demanda[y] = 0
    else:
        #En caso de mayor demanda resto a la demanda el total de la oferta
        demanda[y] = demanda[y] - oferta[x]
        #Se asigna a la matriz de costos la demanda correspondiente para esa celda
        tabla[x][y].demanda = oferta[x]
        #Como la oferta ya fue asignada se cambia la oferta en esa posicion a 0
        oferta[x] = 0

    if oferta[x] == 0:
        #En caso de que la oferta de la fila x haya sido completada se cambia el estado de toda la fila
        cambiarEstadoFila(x, tabla)
    elif demanda[y] == 0:
        #En caso de que la demanda de la columna x haya sido completada se cambia el estado de toda la columna
        cambiarEstadoColumna(y, tabla)

ecuacion = ""
costoFinal = 0
#Se verifica toda la matriz de costos
for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        #Si la demanda no es cero se asigna la ecuacion el costo por la demanda y se suma el costoFinal
        if(tabla[i][j].demanda != 0):
            ecuacion += str(tabla[i][j].costo) + "x" + str(tabla[i][j].demanda) + " + "
            costoFinal += tabla[i][j].costo * tabla[i][j].demanda
#Se elimina el ultimo mas y se concatena con el costoFinal
ecuacion = ecuacion[:-3] + " = " + str(costoFinal)
#se imprime la ecuacion
print(ecuacion)