def summa(u, v):
    c = 299792.458
    uv_summa = ((u + v) / (1 + (u * v) / (c ** 2)))
    return uv_summa
    #dec = int(uv_summa, 16)
    #return dec
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

a = summa(u, v)
b = summa(a, x)
c = summa(b, y)

print("Kiiruste summa on", c, "km/s.")



