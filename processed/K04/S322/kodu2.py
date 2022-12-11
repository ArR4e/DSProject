c = 299792.458

def summa(u, v):
    return (u + v) / (1 + ((u*v)/c**2))

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
v = summa(u, v)
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
x = summa(v, x)
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
y = summa(x, y)
print(f"Kiiruste summa on {y} km/s")
