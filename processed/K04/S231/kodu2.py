# Erirelatiivsusteooria
def summa(u, v):
    return ((u + v) / (1 + (u * v / c ** 2)))
a = float(input("""Esimese keha kiirus
vaatleja suhtes on :"""))
b = float(input("""Teise keha kiirus
vaatleja suhtes on :"""))
d = float(input("""Kolmanda keha kiirus
vaatleja suhtes on :"""))
e = float(input("""Neljanda keha kiirus
vaatleja suhtes on :"""))
c = 299792.458
print(summa(a, b))
print(summa(a, b) + d)
print("Kiiruste summa on")
print((summa(a, b) + d) + e)
print("km/s")




    