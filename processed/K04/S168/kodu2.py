c = 299792.458
def summa(u, v):
    kiirus = (u + v)/ (1 + (u * v)/c**2)
    return kiirus

u = int(input("Esimese keha kiirus vaatleja suhtes on: "))
v = int(input("Teise keha kiirus esimese keha suhtes on: "))
u = float(u)
v = float(v)
t = summa(u, v)
v = int(input("Kolmanda keha kiirus teise keha suhtes on: "))
v = float(v)
u = summa(t, v)
v = int(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
v = float(v)
lõpp = summa(u, v)
print("Kiiruste summa on", lõpp, "km/s.")