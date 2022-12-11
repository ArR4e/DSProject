u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))                
y = float(input("Neljanda keha kiirus vaatleja suhtes on: "))

def summa(u,v):
    kiirus_1 = (u + v) / (1 + ((u * v)/ 299792.458**2))
    kiirus_2 = (kiirus_1 + x) / (1 + ((kiirus_1 * x)/ 299792.458**2))
    kiirus_3 = (kiirus_2 + y) / (1 + ((kiirus_2 * y)/ 299792.458**2))
    return kiirus_3

print("Kiiruste summa on ", summa(u,v), "km/s.")
