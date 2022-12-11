c=299792.458
u = int(input("Esimese keha kiirus vaatleja suhtes on: "))
v = int(input("Teise keha kiirus esimese keha suhtes on: "))
x = int(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = int(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
def summa(u,v):
    return((u+v)/(1+(u*v/(c**2))))
print("Kiiruste summa on", summa(summa(summa(u,v),x),y))