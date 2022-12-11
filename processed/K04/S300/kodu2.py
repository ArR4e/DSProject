def summa(u, v):
    c = 299792.458
    return (u + v) / ((1 + ((u * v) / c**2)))
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
sum1 = summa(u, v)
def summa(sum1, x):
    c = 299792.458
    return (sum1 + x) / ((1 + ((sum1 * x) / c**2)))
sum2 = summa(sum1, x)
def summa(sum2, y):
    c = 299792.458
    return (sum2 + y) / ((1 + ((sum2 * y) / c**2)))
print("Kiiruste summa on", summa(sum2, y), "km/s")