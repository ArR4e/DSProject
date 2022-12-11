import math

u = int(input("Esimese keha kiirus vaatleja suhtes on: "))
v = int(input("Teise keha kiirus esimese keha suhtes on: "))
x = int(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = int(input("Neljanda keha kiirus kolmanda suhtes on: "))
c = 299792.458

def summa(u,v,x,y):
    k_summa = (u + v) /(1 + u * v / c**2)
    print(k_summa)
    x_summa = (k_summa + x) /(1 + k_summa * x / c**2)
    print(x_summa)
    y_summa = (x_summa + y) /(1 + x_summa * y / c**2)
    print("Kiiruste summa on " + str(y_summa) + " km/s")
    
summa(u,v,x,y)