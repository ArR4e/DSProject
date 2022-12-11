def summa(u,v):
    summa=(u+v)/(1+((u*v)/(c**2)))
    return summa

c=299792.458

u=float(input(" Esimese keha kiirus vaatleja suhtes on:"))
v=float(input("Teise keha kiirus esimese keha suhtes on:"))
a=summa(u,v)

x=float(input("Kolmanda keha kiirus teise keha suhtes on:"))
b=summa(a,x)

y=float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))
print(summa(b,y))