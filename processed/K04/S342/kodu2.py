c = 299792.458
u = float(input("u = "))
v = float(input("v = "))
x = float(input("x = "))
y = float(input("y = "))
v1 = 0
def summa(u, v):
    v1 = (u + v) / (1 +((u*v)/c**2))
    return v1
v1 = summa(u, v)
v1 = summa(v1, x)
v1 = summa(v1, y)
print("Esimese keha kiirus vaatleja suhtes on: " + str(round(u)))
print("Teise keha kiirus vaatleja suhtes on: " + str(round(v)))
print("Kolmanda keha kiirus vaatleja suhtes on: " + str(round(x)))
print("Neljanda keha kiirus vaatleja suhtes on: " + str(round(y)))
print("Kiiruste summa on " + str(v1) + " km/s")