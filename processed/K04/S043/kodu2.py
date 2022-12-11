c = 299792.458
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y = float(input("Neljanda keha kiirus vaatleja suhtes on: "))

def summa(a, b):
    return (a+b)/(1+((a*b)/(c*c)))

lopv = summa(summa((summa(u, v)), x), y)

print("Kiiruste summa on", lopv, "km/s")

