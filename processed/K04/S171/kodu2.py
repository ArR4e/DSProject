def summa(u,v):
    return (u + v)/(1+((u*v)/299792.458**2))

a = float(input("Esimese keha kiirus vaatleja suhtes on:"))
b = float(input("Teise keha kiirus esimese keha suhtes on:"))
c = float(input("Kolmanda keha kiirus teise keha suhtes on:"))
d = float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))

i = summa(a,b)
i = summa(i,c)
i = summa(i,d)
print(i)