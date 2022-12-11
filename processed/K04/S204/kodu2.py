
u = float(input("1. keha kiirus vaatleja suhtes on: "))
v = float(input("2. keha kiirus vaatleja suhtes on: "))
x = float(input("3. keha kiirus vaatleja suhtes on: "))
y = float(input("4. keha kiirus vaatleja suhtes on: "))

def summa(u,v):
    return((u+v)/(1+(u*v/(299792,458)**2)))
summa=summa(u,v)
