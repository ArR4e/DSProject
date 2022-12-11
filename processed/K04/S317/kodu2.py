u1 = input("Esimese keha kiirus vaatleja suhtes: ")
u = float(u1)
v1 = input("Teise keha kiirus vaatleja suhtes: ")
v = float(v1)
x1 = input("Kolmanda keha kiirus vaatleja suhtes: ")
x = float(x1)
y1 = input("Neljanda keha kiirus vaatleja suhtes: ")
y = float(y1)
c = 299792.458
def summa(u, v):
    uv = float((u + v)/(1 + (u * v)/c**2))
    return uv
uv = summa(u, v)
def summa1(uv, x):
    uvx = (uv + x)/(1 + (uv * x)/c**2)
    return  uvx
uvx = summa1(uv, x)
def summakokku(uvx, y):
    uvxy = (uv + xy)/(1 + (uv * xy)/c**2)
    return uvxy
uvxy = summa1(uvx, y)
print(uvxy, "km/s")


