c=299792.458 #Valguse kiirus

def summa(u,v):
    return (u+v)/(1+((u*v)/(c**2)))

u=float(input("Esimese keha kiirus vaatleja suhtes: "))
v=float(input("Teise keha kiirus esimese suhtes: "))
x=float(input("Kolmanda keha kiirus teise suhtes: "))
y=float(input("Neljanda keha kiirus kolmanda suhtes: "))

print("Kiiruste summa on ",summa(summa(summa(u,v),x),y)," km/h")