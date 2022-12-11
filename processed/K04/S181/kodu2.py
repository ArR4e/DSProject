def summa(u,v):
    return (u+v)/(1+(u*v)/c**2)


nr1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
nr2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
nr3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
nr4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

c =  299792.458

sum1 = summa(nr1,nr2)
sum2 = summa(nr3,nr4)
sum = summa(sum1,sum2)
print("Kiiruste summa on "+str(sum)+" km/s")