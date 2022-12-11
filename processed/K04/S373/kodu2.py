def summa(u, v):
    return float((u+v)/(1+((u*v)/c**2)))
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y = float(input("Neljanda keha kiirus vaatleja suhtes on: "))
c = 299792.458
summaa = summa(u, v)
summa_ = summa(summaa, x)
lahendus = summa(summa_, y)
print("Kiiruste summa on: " + str(lahendus) + " km/s")
