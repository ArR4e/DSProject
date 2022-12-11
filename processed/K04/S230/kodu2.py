u=float(input("Esimese keha kiirus vaatleja suhtes: "))
v=float(input("Teise keha kiirus esimese keha suhtes: "))
x=float(input("Kolmanda keha kiirus teise keha suhtes: "))
y=float(input("Neljanda keha kiirus kolmanda keha suhtes: "))
c=299792.458
def summa(u,v):
    return((u+v)/(1+(u*v)/(c*c)))
a=summa(u,v)
a=summa(a,x)
a=summa(a,y)
print("Kiiruste summa on",a,"km/h")