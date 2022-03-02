#Autor: Bryant Ortega
#Fecha creación: 13/02/2022
#Se importa la libreria
from gekko import GEKKO
#Se inicializa el objeto GEKKO con la opcion remote=False para indicar que no se esta conectando a un servidor remoto
m = GEKKO(remote=False)
#Se crean las variables con un valor minimo de 0
x1 = m.Var(lb=0)
x2 = m.Var(lb=0)
#Se indica la funcion objetivo y que se desea hacer si Maximizar o Minimizar
m.Maximize(2*x1+x2)
#Se agregan las inecuaciones y ecuaciones al objeto gekko
m.Equation(x1+x2==2)
m.Equation(2*x1+3*x2>=5)
m.Equation(x1+2*x2<=3)
#Orden para iniciar a resolver el sistema
m.solve(disp=False)
#Se almacenan los resultados en variables
res1 = round(x1.value[0],2)
res2 = round(x2.value[0],2)
#resultado que se calculó para Z
resZ = round(m.options.OBJFCNVAL,2)*-1
print("X1 = " + str(res1))
print("X2 = " + str(res2))
print("Z = " + str(resZ))