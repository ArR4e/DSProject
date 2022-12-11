def summa(u, v):
    c=299792.458
    valem=(u+v)/(1+((u*v)/c**2))
    return valem
x = float(input("Esimese keha kiirus vaatleja suhtes on: "))
y = float(input("Teise keha kiirus esimese keha suhtes on: "))
z = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
g = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
summa1 = (summa(x, y))
summa2 = (summa(summa1, z))
lõpptulemus = (summa(summa2, g))
print("Kiiruste summa on", lõpptulemus, "km/s")