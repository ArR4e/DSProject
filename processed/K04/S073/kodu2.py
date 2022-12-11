c = 299792.458

def summa(u, v):
    u = float(u)
    v = float(v)
    return (u+v)/(1+((u*v)/(c*c)))

a = input("Esimese keha kiirus vaatleja suhtes on:" )
b = input("Teise keha kiirus esimese keha suhtes on: ")
d = input("Kolmanda keha kiirus teise keha suhtes on: ")
e = input("Neljanda keha kiirus kolmanda keha suhtes on: ")

print(f"Kiiruste summa on {summa(summa(summa(a, b), d), e),2} km/s")