c=299792.458

def summa(u,v):
    return (u+v)/(1+u*v/c**2)

u=float(input('Esimese keha kiirus vaatleja suhtes on:'))
v=float(input('Teise keha kiirus esimese keha suhtes on:'))
x=float(input('Kolmanda keha kiirus teise keha suhtes on:'))
y=float(input('Neljanda keha kiirus kolmanda keha suhtes on:'))

a=summa(u,v)
b=summa(a,x)

print(summa(b,y),'km/s')