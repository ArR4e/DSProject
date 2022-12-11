es = float(input("Esimese keha kiirus vaatleja suhtes on: "))
tes = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
c = 299792.458

def summa(u, v):
    valem = (u + v) / (1 + (u*v)/(c**2))
    return valem


vov = summa(es, tes)
wow = summa(vov, x)
wwoww = summa(wow, y)




print("Kiiruste summa on ", str(wwoww), "km/s")   