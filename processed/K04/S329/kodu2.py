def summa1(u, v):
    return((u+v)/ (1+ u*v/299792.458**2))
    print(summa1(u, v))

def summa2(summa1, x):
    return((summa1+x)/ (1+ summa1*x/299792.458**2))
    print(summa2(summa1, x))

def summa(summa2, y):
    return((summa2+y)/ (1+ summa2*y/299792.458**2))
    print(summa2(summa1, y))

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on", summa(summa2(summa1(u, v), x), y), "km/s.")







