def summa (u, v):
    c = 299792.458
    summa =((u+v)/(1+((u*v)/c**2)))
    return summa



u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

kokku = summa(u, v)
kokku = summa(kokku, x)



print("Kiiruste summa on " + str(summa(kokku, y)) + " km/s")
