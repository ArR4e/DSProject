def summa(u, v):
    c = 299792.458
    
    sein = ((u + v) / (1 + ((u*v)/(c**2))))
    return sein

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
ein = summa(u, v)
ste = summa(x,ein)
ini = summa(y,ste)
print("Kiiruste summa on " + str(ini) + " km/s")