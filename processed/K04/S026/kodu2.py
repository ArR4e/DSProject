u = float(input("Sisesta esimese keha kiirus: "))
v = float(input("Sisesta teise keha kiirus: "))
x = float(input("Sisesta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha kiirus: "))
c = 299792.458

summa_uv = (u + v) / (1 + (u * v / c**2))
summa_vx = (v + x) / (1 + (v * x / c**2))
summa_xy = (x + y) / (1 + (x * y / c**2))
summa_uvx = (summa_uv + x) / (1 + (summa_uv * x / c**2))
summa_uvxy = (summa_uvx + y) / (1 + (summa_uvx * y / c**2))

print("Esimese keha kiirus vaatleja suhtes on: ", u)
print("Teise keha kiirus esimese keha suhtes on: ", summa_uv)
print("Kolmanda keha kiirus teise keha suhtes on: ", summa_vx)
print("Neljanda keha kiirus kolmanda keha suhtes on: ", summa_xy)
print("Kiiruste summa on ", summa_uvxy, "km/s")

#Ma pole päris kindel, kuidas selles ülesandes kasutada funktsiooni.