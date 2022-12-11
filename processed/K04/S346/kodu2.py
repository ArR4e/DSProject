def summa(u, v):
    c = 299792.458
    sum1 = (u + v) / (1 + (u*v/c**2))
    return sum1
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
summa(summa(u,v),x)
summa(summa(summa(u,v),x), y)
print("Kiiruste summa on ", summa(summa(summa(u,v),x), y), "km/s")