u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus esimese keha suhtes on: "))
x=float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y=float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))


def summa(u,v):
    c=299792.458
    return (u+v)/(1+u*v/c**2)

a=summa(u,v)
b=summa(a,x)
c=summa(b,y)
 

print("Kiiruste summa on "+str(c)+" km/s.")

      