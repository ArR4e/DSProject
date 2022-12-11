u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus vaatleja suhtes on: "))
x=str(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y=str(input("Neljanda keha kiirus vaatleja suhtes on: "))


c=float(299792.458)

def summa(u,v):   
    kiirus = (u+v)/(1+(u*v)/(c**2))
    return(kiirus)

if x=="":
    x=0
else:
    x=float(x)
    
if y=="":
    y=0
else:
    y=float(y)


kiirus=summa(u,v)
kiirus=summa(kiirus,x)
kiirus=summa(kiirus,y)

print(str(kiirus) + str(" km/h"))
    