c = 299792.458

def summa(u, v):
    return (u + v) / (1 + (u * v) / c ** 2)

    
u = float(input("Esimese keha kiirus vaatleja suhtes on:"))
v = float(input("Teise keha kiirus vaatleja suhtes on:"))
x = float(input("Kolmanda keha kiirus vaatleja suhtes on:"))
y = float(input("Neljanda keha kiirus vaatleja suhtes on:"))

summa(u, v)

summa2 = (summa(u, v) + x) / (1 + (summa(u, v) * x) / c ** 2)
summa3 = (summa2 + y) / (1 + (summa2 * y) / c ** 2)
print("Kiiruste summa on", summa3, "km/s")
