c = 299792.458
i = 0

while True:
    if i>2:
        break
    
    if i == 0:
        u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
        v = float(input("Teise keha kiirus esimese keha suhtes on: "))
    if i == 1:
        u = summa(u, v)
        v = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
    if i == 2:
        u = summa(u, v)
        v = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
    def summa(u, v):
        return (u + v)/(1 + (u*v)/(c*c))
    
    i += 1

print("Kiiruste summa on", summa(u, v), "km/s.")
