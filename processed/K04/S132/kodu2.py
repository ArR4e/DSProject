def summa(u, v):
    x = (u + v) / (1 + ((u * v) / (299792.458 ** 2)))
    return x

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
kiiruste_summa = summa(y, summa(x, summa(u, v)))
print(f"Kiiruste summa on {kiiruste_summa} km/s")