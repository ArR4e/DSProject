u = float(input("Sisesta esimese keha kiirus vaatleja suhtes (km/s): "))
v = float(input("Sisesta teise keha kiirus vaatleja suhtes (km/s): "))
x = float(input("Sisesta kolmanda keha kiirus vaatleja suhtes (km/s): "))
y = float(input("Sisesta neljanda keha kiirus vaatleja suhtes (km/s): "))


c = 299792.458

def summa(u,v):
    return ((u + v)/(1+(u*v)/(c**2)))

print("Kiiruste summa on: ",summa(summa(summa(u,v), x), y), "km/s")

