def summa(u, v):
    c = 299792.458
    summa = (u + v) / (1 + ((u * v) / (c ** 2)))
    return summa

u = float(input("Sisesta esimese keha kiirus (km/s) vaatleja suhtes: "))
v = float(input("Sisesta teise keha kiirus (km/s) esimese keha suhtes: "))
x = float(input("Sisesta kolmanda keha kiirus (km/s) teise keha suhtes: "))
y = float(input("Sisesta neljanda keha kiirus (km/s) kolmanda keha suhtes: "))
üldsumma = summa(summa(summa(u, v), x), y)

print("Kiiruste summa on " + str(üldsumma) + " km/s.")