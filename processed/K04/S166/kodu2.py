c = 299792.458
m=0

def summa(u,v):
     return (u+v)/(1+(u*v/(c**2)))


u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

m = summa(summa(summa(u,v),x),y)


print("Kiiruste summa on ",m, " km/s")