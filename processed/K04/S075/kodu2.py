def summa(u,v):
    c=299792.458
    return ((u)+(v))/(1+(((u)*(v))/(c*c)))

u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus esimese keha suhtes on: "))
x=float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y=float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

a=summa(u,v)
b=summa(a,x)
l=summa(b,y)

print("Kiiruste summa on "+str(l)+" km/s")