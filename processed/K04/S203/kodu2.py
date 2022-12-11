def summa(u, v):
    summa1 = (u + v) / ( 1 + (u * v) / c **2)
    return summa1

c = 299792.458

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

a = summa(x, summa(u, v))
b = summa(y, a)

print("Kiiruste summa on: ", b)