u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
c = 299792.458
k1 = (u + v) /(1 + (u*v)/(c*c))
k2 = (k1 + x) /(1 + (k1*x)/(c*c))
k3 = (k2 + y) /(1 + (k2*y)/(c*c))
print(" Kiiruste summa on", k2 , "km/s")