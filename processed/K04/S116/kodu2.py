c = 299792.458

x = float(input("Esimese keha kiirus vaatleja suhtes: "))
y = float(input("Teise keha kiirus esimese keha suhtes: "))
z = float(input("Kolmanda keha kiirus teise keha suhtes: "))
u = float(input("Neljanda keha kiirus kolmanda keha suhtes: "))


def summa(u,v):
    return (u+v)/(1+u*v/c**2)

print(summa(summa(summa(x,y),z),u))