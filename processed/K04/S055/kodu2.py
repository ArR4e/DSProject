c = 299792.458 # km/s

def summa(u,v):
    return (u + v) / (1 + (u*v)/(c*c))

k1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
k2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
k3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
k4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on", summa(k4, summa(k3, summa(k2, k1))), "km/s")
    