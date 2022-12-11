def summa(u,v):
    v1=(u+v)/(1+((u*v)/c**2))
    v2=(v1+x)/(1+((v1*x)/c**2))
    return (v2+y)/(1+((v2*y)/c**2))



u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus esimese keha suhtes on: "))
x=float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y=float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))


c=299792.458
summa(u,v)
print(summa(u,v))