a = float(input("Esimese keha kiirus vaatleja suhtes on:"))
b = float(input("Teise keha kiirus esimese keha suhtes on:"))
c = float(input("Kolmanda keha kiirus teise keha suhtes on:"))
d = float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))
k = 299792.458
def summa(a, b):
    summa = (a+b)/(1+(a*b/k**2))
    return summa
def summa1(summa, c):
    summa1 = (summa+c)/(1+(summa*c/k**2))
    return summa1
def summa2(summa1, d):
    summa2 = (summa1+d)/(1+(summa1*d/k**2))
    return summa2
summa = summa(a, b)
summa1 = summa1(summa, c)
summa2 = summa2(summa1, d)
print("Kiiruste summa on",summa2, "km/s")
    