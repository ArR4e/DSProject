c = 299792.458

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus keha suhtes on: "))
x = float(input("Kolmanda keha kiirus keha suhtes on: "))
y = float(input("Neljanda keha kiirus keha suhtes on: "))

def summa(u, v):
    return (u+v)/(1+((u*v)/c**2))

arvutus1 = summa(u, v)
arvutus2 = summa(arvutus1, x)
kogu_summa = summa(arvutus2, y)

print("Kiiruste summa on " + str(kogu_summa) + " km/s")

