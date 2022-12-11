def summa(u,v):
    return((u + v) / (1 + ((u*v) / (299792.458**2))))
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
a = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
b = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
print("Kiiruste summa on", str(summa(u,summa(v,summa(a,b)))), "km/s")