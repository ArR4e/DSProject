def summa(u,v):
    return (u + v) / (1 + ((u*v)/c**2))

c = 299792.458
u = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
v = float(input("Sisesta teise keha kiirus esimese keha suhtes: "))
u = summa(u,v)
v = float(input("Sisesta kolmanda keha kiirus teise keha suhtes: "))
u = summa(u,v)
v = float(input("Sisesta neljanda keha kiirus kolmanda keha suhtes: "))


print("Kiiruste summa on ", summa(u,v), "km/s")