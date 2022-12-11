u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus esimese keha suhtes on: "))
x=input("Kolmanda keha kiirus teise keha suhtes on: ")
y=input("Neljanda keha kiirus kolmanda keha suhtes on: ")
def summa(u,v):
    try:
        x.isdigit()
        võrrand1=(u+v)/(1+((u*v)/299792.458**2))
        võrrand2=(võrrand1+float(x))/(1+((võrrand1*float(x))/299792.458**2))
        võrrand3=(võrrand2+float(y))/(1+((võrrand2*float(y))/299792.458**2))
        return võrrand3
    except:
        võrrand1=(u+v)/(1+((u*v)/299792.458**2))
        return võrrand1
print("Kiiruste summa on ",summa(u,v), " km/s.")