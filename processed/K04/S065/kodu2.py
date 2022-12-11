# 2. Einsteini erirelatiivsusteooria

def summa(u,v):
    c = 299792.458 # valguse kiirus (ühik: km/s)
    murru_lugeja = u + v
    murru_nimetaja = 1 + ((u*v)/(c**2))
    valem = murru_lugeja/murru_nimetaja
    return valem

a = float(input("Esimese keha kiirus vaatleja suhtes on: "))
b = float(input("Teise keha kiirus vaatleja suhtes on: "))
c = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
d = float(input("Neljanda keha kiirus teise keha suhtes on: "))

print(summa(summa(summa(a,b),c),d))