def summa(u,v):
    return (u+v)/(1+((u*v)/(299792.458**2)))

u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus vaatleja suhtes on: "))
x=float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y=float(input("Neljanda keha kiirus vaatleja suhtes on: "))

sum1=summa(u,v)
sum2=summa(sum1,x)
sum3=summa(sum2,y)
print("Kiiruste summa on "+str(sum3)+" km/s.")

    