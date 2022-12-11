def summa(u, v):
    kiirus = (u + v)/(1 + u * v/299792.458**2)
    return kiirus

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y = float(input("Neljanda keha kiirus vaatleja suhtes on: "))

kiirus = summa(u, v)
kiirus = summa(kiirus, x)
kiirus = summa(kiirus, y)

print("Kiiruste summa on", kiirus, "km/s")