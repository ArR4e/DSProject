u = int(input("Esimese keha kiirus vaatleja suhtes on: "))

v = int(input("Teise keha kiirus esimese keha suhtes on: "))

x = int(input("Kolmanda keha kiirus teise keha suhtes on: "))

y = int(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

c = 299792.458

def summa(u, v):
    x >= 0
    y >= 0
    return (((((((u + v)/(1 + ((u*v)/(c**2)))) + x))/((1 + (((u + v)/(1 + ((u*v)/(c**2))))*x)/(c**2)))) + y))/(1 + (((((((u + v)/(1 + ((u*v)/(c**2)))) + x))/((1 + (((u + v)/(1 + ((u*v)/(c**2))))*x)/(c**2))))*y)/c**2))
print("Kiiruste summa on ", summa(u, v), "km/s")
    