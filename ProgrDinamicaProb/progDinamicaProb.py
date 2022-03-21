#Autor: Bryant Ortega
#Fecha creación: 20/03/2022

#Definición de variables
num_etapas = 3
penalizacion = 16
costo_producto = 1
probabilidad_ningun_prod = 1/2

#Valor de encender la maquina 0 si no se enciende y 3 si se enciende
def k(X_n):
    return 0 if X_n == 0 else 3

#Funcion de costo recursiva que trae el costo minimo y que X_n cumplen ese costo minimo
def func_costo_min(n):
    resultado = []
    #Si el n es mayor o igual a cuatro va a valer la penalizacion 
    if n >= 4:
        return (penalizacion,resultado)
    else:
        #Si es la primera serie tiene que producir al menos un producto
        X_n = 0 if n == 0 else 1
        nueva_pena = 0
        while(True):
            #Calcula cual sera el costo minimo del X_n actual y el siguiente
            actual = k(X_n) + X_n + (probabilidad_ningun_prod**X_n)*func_costo_min(n+1)[0]
            sig = k(X_n + 1) + (X_n + 1) + (probabilidad_ningun_prod**(X_n+1))*func_costo_min(n+1)[0]
            #Verifica si el siguiente es mas grande y sale del ciclo, si es igual agrega al resultado el valor actual de Xn, si es mayor reinicia los resultados
            if sig>actual:
                resultado.append(X_n)
                nueva_pena = actual
                break
            elif sig == actual:
                resultado.append(X_n)
                nueva_pena = actual
            else:
                resultado = []
            #Va aumentando los X_n desde 0 hasta que la condicion anterior salga del ciclo
            X_n+=1
        return (nueva_pena,resultado)

#Retorna el valor de la funcion de costo para cierto x_n y n
def func_costo(n, X_n):
    if n >= 4:
        return penalizacion
    else:
        return k(X_n) + X_n + (probabilidad_ningun_prod**X_n)*func_costo_min(n+1)[0]

res_final = []
#Recorre de forma descendente las etapas
for i in range(num_etapas,0,-1):
    #Verifica que X_n es el maximo en los resultados y le suma 2 posiciones mas el 0 y el siguiente numero para que se aprecie el cambio en la funcion de costo
    maximo = max(func_costo_min(i)[1]) + 2
    #Se definen la cantidad de espacios para cada tabla
    espacios = 5 if maximo > 4 else 6
    #Se calcula el total de espacios para colorcar de manera grafica
    total_espacios = (espacios*maximo*2) + (maximo * 2) 
    #Se calcula los espacios que debe tener la celda mas grande
    espacio_h = (total_espacios - 42)//2
    #Se imprimen las cabeceras
    print("-"*(total_espacios+24))
    print("\\X"+str(i)+"|"+ " "*espacio_h+"Fn(X"+str(i)+") = K(X"+str(i)+") + X"+str(i)+" + [(1/2)^(X"+str(i)+")][Fn+1*]"+ " "*espacio_h+"|  Fn*(S"+str(i)+")  |  X"+str(i)+"*  |")
    
    print(" \\ |"+"-"*(total_espacios-1)+"|"+" "*11+"|"+" "*7+"|")
    print("S"+str(i)+"\\",end="")
    
    #Se colocan los X_n desde 0 hasta el maximo
    for j in range(0, maximo):
        print("|"+" "*espacios+str(j)+" "*espacios, end="")
    print("|"+" "*11+"|"+" "*7+"|")
    print("-"*(total_espacios+24))
    #Si es la primera serie se debe encender la maquina siempre por lo que no se contempla el 0
    if(i != 1):
        print(" "+str(0)+" ",end="")
        for j in range(0, maximo):
            print("|"+" "*espacios+"0"+" "*espacios, end="")
        print("|"+" "*5+"0"+" "*5+"|"+" "*3+"0"+" "*3+"|")
    #Se imprime cuando la maquina se enciende
    print(" 1 ",end="")
    for j in range(0, maximo):
        #se calcula el costo por cada X_n y si es un entero se quitan las dos ultimas posiciones que son .0
        costo = func_costo(i,j)
        val = str(round(costo, 2))
        if(costo.is_integer()):
            val = val[:-2]
        #Se calculan los espacios necesarios para que la tabla no se deforme
        espacio_completo = (espacios*2) + 1  
        n_espacio = (espacio_completo - len(val)) // 2
        #Se imprime la funcion de costo para cada X_n
        print("|"+" "*n_espacio+val+" "*(espacio_completo - len(val) - n_espacio), end="")
    #Se calculan los espacios para la funcion de costo minima
    costo = func_costo_min(i)
    val = str(round(costo[0], 2))
    if(costo[0].is_integer()):
        val = val[:-2]
    espacio_completo1 = 11
    n_espacio1 = (espacio_completo1 - len(val)) // 2

    #Se calcula los espacios para los X_n que cumplen con la funcion de costo minima
    val2 = ' o '.join(map(str, costo[1]))
    espacio_completo2 = 7
    n_espacio2 = (espacio_completo2 - len(val2)) // 2
    res_final.append((val, val2))

    #se imprimie la funcion de costo minima y los X_n que cumplen
    print("|"+" "*n_espacio1+val+" "*(espacio_completo1-n_espacio1-len(val))+"|"+" "*n_espacio2+val2+" "*(espacio_completo2-n_espacio2-len(val2))+"|")
    print("-"*(total_espacios+24))
    #Se imprimen las conclusiones por serie
    print("La cantidad de productos a producir son "+val2+" para reducir el costo a "+val)
    
#Se imprimen las conclusiones finales
serie = 1
print("La política óptima es producir")
for k in range(len(res_final) - 1, -1, -1):
    print(res_final[k][1] +" artículos en la serie " + str(serie) + " de producción",end="")
    if k != 0:
        print("; si ninguno fuera aceptable, entonces habría que producir")
    serie += 1
