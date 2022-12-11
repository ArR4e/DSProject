def summa(u, v):
    c = 299792.458
    summa_üks = ((u+v)/(1 + u * v / c ** 2))
    summa_kaks = ((summa_üks + x)/(1 + summa_üks * x / c ** 2))
    summa_kolm = ((summa_kaks + y)/(1 + summa_kaks * y / c ** 2))
    return summa_kolm
    
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on " + str(summa(u, v)) + " km/s")
