c=299792.458

def summa(u,v):
        return (u+v)/(1+(u*v)/c**2)

u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus vaatleja suhtes on: "))
x=float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y=float(input("Neljanda keha kiirus vaatleja suhtes on: "))

sum=summa(summa(summa(u,v),x),y)

print("Kiiruste summa on",str(sum),"km/s.")