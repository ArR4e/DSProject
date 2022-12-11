def summa(u, v):
    return (u+v)/(1+((u*v)/(c**2)))

c = 299792.458

v1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v2 = float(input("Teise keha kiirus vaatleja suhtes on: "))
v3 = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
v4 = float(input("Neljanda keha kiirus vaatleja suhtes on: "))

x = float(summa(v1, v2))
y = float(summa(x, v3))
z = float(summa(y, v4))

print("Kiiruste summa on " + str(z) + " km/s")
