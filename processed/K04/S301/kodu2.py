a = float(input("Esimese keha kiirus vaatleja suhtes on: "))
b = float(input("Teise keha kiirus esimese keha suhtes on: "))
c = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
d = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

def summa(u, v):
    c = 299792.458
    return (u + v)/ (1+ (u*v)/c**2)
summ = summa(0, a)
summa1 = summa(a, b)
summa2 = summa(summa1, c)
summa3 = summa(summa2, d)
print("kiiruste summa on: " + str(summa3) + "km/h")
