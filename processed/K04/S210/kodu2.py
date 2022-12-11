def summa(u,v):
    c = 299792.458
    return((u + v) / (1 + (u*v/c**2)))
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y = float(input("Neljanda keha kiirus vaatleja suhtes on: "))
print("Kiiruste summa on " + str(summa(summa(summa(u,v), x), y)) + " km/s")