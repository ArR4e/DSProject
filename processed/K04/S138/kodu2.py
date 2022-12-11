def summa(u,v):
    c = 299792.458
    return float((u+v)/(1+(u*v)/c**2))

x1 = float(input("Esimese keha kiirus vaatleja suhtes on:"))
x2 = float(input("Teise keha kiirus esimese keha suhtes on:"))
x3 = float(input("Neljada keha kiirus kolmanda keha suhtes on:"))
x4 = float(input("Neljada keha kiirus kolmanda keha suhtes on:"))

y1 = summa(x1,x2)
y2 = summa(y1,x3)
y3 = summa(y2,x4)

print("Kiiruste summa on "+str(y3)+" km/s")