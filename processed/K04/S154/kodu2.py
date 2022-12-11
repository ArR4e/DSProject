from math import *
u = int(input("Esimese keha kiirus vaatleja suhtes: "))
v = int(input("Teise keha kiirus esimese keha suhtes on: "))
x = int(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = int(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

k = 0

c = 299792.458

def summa(u, v, x, y):
    k = (u + v) / (1 + (u*v)/c**2)
    k = (k + x) / (1 + (k*x)/c**2)
    k = (k + y) / (1 + (k*y)/c**2)
    return k
print(summa(u, v, x, y), " km/s")
