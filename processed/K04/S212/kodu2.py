def summa(u,v):
    sum = (u+v)/(1+(u*v/(c**2)))
    return sum
    
c = 299792.458 #(km/s)

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on", str(summa(summa(summa(u,v),x),y)), "km/s")