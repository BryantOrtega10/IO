import re
from gekko import GEKKO
m = GEKKO(remote=False)
x1 = m.Var(lb=0)
x2 = m.Var(lb=0)
m.Minimize(x1+x2)
m.Equation(5*x1+3*x2>=45)
m.Equation(3*x1+2*x2>=34)
m.Equation(1*x1+4*x2==20)
m.solve(disp=False)

print("X1 = " + str(x1.value[0]))
print("X2 = " + str(x2.value[0]))
print("Z = " + str(round(m.options.OBJFCNVAL)))