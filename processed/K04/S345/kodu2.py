def summa(esimene, teine):
    c = 299792.458
    return (esimene+teine)/(1+(esimene*teine)/c**2)

u = int(input("Esimese keha kiirus vaatleja suhtes on: "))
v = int(input("Teise keha kiirus esimese keha suhtes on: "))
x = int(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = int(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

uv = summa(u, v)
uvx = summa(uv, x)
uvxy = summa(uvx, y)

print("Kiiruste summa on " + str(uvxy) + " km/s")