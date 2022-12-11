def summa(a, b):
    return (a + b) / (1 + (a * b) / 299792.458 ** 2)

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmas keha kiirus teise keha suhtes on: "))
y = float(input("Neljas keha kiirus kolmanda keha suhtes on: "))
 
print(summa(summa(summa(u, v), x), y))