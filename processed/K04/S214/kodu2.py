def summa(u, v):
    return (u+v)/(1+((u*v)/(c**2)))
c = 299792.458
u = float(input("Esimese keha kiirus vaatleja suhtes: "))
v = float(input("Teise keha kiirus esimese keha suhtes: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes: "))
a = summa(u,v)
b = summa(a,x)
d = summa(b,y)
print("Kiiruste summa on",str(d),"km/s.")