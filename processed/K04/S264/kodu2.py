
u = int(input("Esimese keha kiirus vaatleja suhtes on: "))
v = int(input("Teise keha kiirus esimese keha suhtes on: "))
x = int(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = int(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

c = 299792,458

def summa(u, v):
    return (u + v)/(1 + ((u*v)/c**2))


summa1 = summa(summa(u,v),summa(x,y))
print(summa1)