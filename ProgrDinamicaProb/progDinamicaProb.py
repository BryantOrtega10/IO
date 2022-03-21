#Autor: Bryant Ortega
#Fecha creación: 20/03/2022

num_etapas = 3
penalizacion = 16
costo_producto = 1
probabilidad_ningun_prod = 1/2


def k(X_n):
    return 0 if X_n == 0 else 3

def func_costo_min(n):
    resultado = []
    if n >= 4:
        return (penalizacion,resultado)
    else:
        
        X_n = 0 if n == 0 else 1
        nueva_pena = 0
        while(True):
            actual = k(X_n) + X_n + (probabilidad_ningun_prod**X_n)*func_costo_min(n+1)[0]
            sig = k(X_n + 1) + (X_n + 1) + (probabilidad_ningun_prod**(X_n+1))*func_costo_min(n+1)[0]
            
            if sig>actual:
                resultado.append(X_n)
                nueva_pena = actual
                break
            elif sig == actual:
                resultado.append(X_n)
                nueva_pena = actual
            else:
                resultado = []
            X_n+=1
        return (nueva_pena,resultado)


def func_costo(n, X_n):
    if n >= 4:
        return penalizacion
    else:
        return k(X_n) + X_n + (probabilidad_ningun_prod**X_n)*func_costo_min(n+1)[0]

res_final = []
for i in range(num_etapas,0,-1):
    maximo = max(func_costo_min(i)[1]) + 2
    espacios = 5 if maximo > 4 else 6
    total_espacios = (espacios*maximo*2) + (maximo * 2) 
    espacio_h = (total_espacios - 42)//2
    
    print("-"*(total_espacios+24))
    print("\\X"+str(i)+"|"+ " "*espacio_h+"Fn(X"+str(i)+") = K(X"+str(i)+") + X"+str(i)+" + [(1/2)^(X"+str(i)+")][Fn+1*]"+ " "*espacio_h+"|  Fn*(S"+str(i)+")  |  X"+str(i)+"*  |")
    
    print(" \\ |"+"-"*(total_espacios-1)+"|"+" "*11+"|"+" "*7+"|")
    print("S"+str(i)+"\\",end="")
    
    
    for j in range(0, maximo):
        print("|"+" "*espacios+str(j)+" "*espacios, end="")
    print("|"+" "*11+"|"+" "*7+"|")
    print("-"*(total_espacios+24))
    if(i != 0):
        print(" "+str(0)+" ",end="")
        for j in range(0, maximo):
            print("|"+" "*espacios+"0"+" "*espacios, end="")
        print("|"+" "*5+"0"+" "*5+"|"+" "*3+"0"+" "*3+"|")
        
    print(" 1 ",end="")
    for j in range(0, maximo):
        costo = func_costo(i,j)
        val = str(round(costo, 2))
        if(costo.is_integer()):
            val = val[:-2]
        espacio_completo = (espacios*2) + 1  
        n_espacio = (espacio_completo - len(val)) // 2

        print("|"+" "*n_espacio+val+" "*(espacio_completo - len(val) - n_espacio), end="")

    costo = func_costo_min(i)
    val = str(round(costo[0], 2))
    if(costo[0].is_integer()):
        val = val[:-2]
    espacio_completo1 = 11
    n_espacio1 = (espacio_completo1 - len(val)) // 2


    val2 = ' o '.join(map(str, costo[1]))
    espacio_completo2 = 7
    n_espacio2 = (espacio_completo2 - len(val2)) // 2
    res_final.append((val, val2))

    
    print("|"+" "*n_espacio1+val+" "*(espacio_completo1-n_espacio1-len(val))+"|"+" "*n_espacio2+val2+" "*(espacio_completo2-n_espacio2-len(val2))+"|")
    print("-"*(total_espacios+24))
    
    print("La cantidad de productos a producir son "+val2+" para reducir el costo a "+val)
    
serie = 1
print("La política óptima es producir")
for k in range(len(res_final) - 1, -1, -1):
    print(res_final[k][1] +" artículos en la serie " + str(serie) + " de producción",end="")
    if k != 0:
        print("; si ninguno fuera aceptable, entonces habría que producir")
    serie += 1


print()