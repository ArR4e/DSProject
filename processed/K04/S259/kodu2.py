def summa(a, b):
    c = 299792.458
    summa = a + b
    erirelatiivsus = (summa/(1+((a*b)/(c*c))))
    return erirelatiivsus
u = float(input("Esimese keha kiirus vaatleja suhtes: "))
v = float(input("Teise keha kiirus esimese keha suhtes: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes: "))
print("Kiiruste summa on ",summa(summa(summa(u, v), x), y), "km/s")