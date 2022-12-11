def summa(u, v):
    c = 299792.458 # km/s
    x = (u + v)/(1+u*v/c**2)
    
    return x

u = float(input("Esimese keha kiirus vaatleja suhtes: "))
v = float(input("Teise keha kiirus esimese keha suhtes: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes: "))

esimene = summa(u,v)
teine = summa(esimene, x)
kolmas = summa(teine, y)

print(kolmas)