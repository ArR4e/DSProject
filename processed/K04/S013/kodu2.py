
def summa(a,b):
    lugeja = a + b
    nimetaja = 1 + ((a*b)/(c**2))
    f = lugeja / nimetaja
    return f

    
    
c = 299792.458
u =float(input("Esimese keha kiirus vaatleja suhtes on: "))
v =float(input("Teise keha kiirus esimes keha suhtes on: "))
x =float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y =float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
f = summa(u,v)
f = summa(f,x)
summa(f,y)
print("Kiiruste summa on", summa(f,y), "km/s")