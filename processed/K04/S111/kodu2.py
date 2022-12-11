def summa(u,v):
    kiirus1=float((u+v)/(1+u*v/float(c)**2))
    return kiirus1
    
u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus vaatleja suhtes on: "))
x=float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y=float(input("Neljanda keha kiirus vaatleja suhtes on: "))
c=299792.458
        
kiirus1=float(summa(u,v))
kiirus2=float(summa(kiirus1, x))
kiirus3=float(summa(kiirus2,y))
print ("Kiiruste summa on " + str(kiirus3) + " km/h")