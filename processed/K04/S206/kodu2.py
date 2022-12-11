
def summa(u, v):
    c = 299792.458
    return (u+v)/(1+((u*v)/c**2))

a = float(input("Esimese keha kiirus vaatleja suhtes: "))
b = float(input("Teise keha kiirus esimese suhtes: "))
c = float(input("Kolmanda keha kiirus teise suhtes: "))
d = float(input("Neljanda keha kiirus kolmanda suhtes: "))

print("Kiiruste summa on", summa(summa(summa(a, b), c), d), "km/s.")
