def summa (u , v):
    c = 299792.458
    return (u + v) / (1 + ((u * v) / c ** 2))
u = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
v = float(input("Esimese keha suhtes on teise keha kiirus: "))
x = float(input("Teise keha suhtes on kolmanda keha kiirus: "))
y = float(input("Kolmanda keha suhtes on neljanda keha kiirus: "))
summa_1 = summa(u , v)
def summa (summa_1 , x):
    c = 299792.458
    return (summa_1 + x) / (1 + ((summa_1 * x) / c ** 2))
summa_2 = summa(summa_1 , x)
def summa(summa_2 , y):
    c = 299792.458
    return (summa_2 + y) / (1 + ((summa_2 * y) / c ** 2))
print("Kehade kiiruste summa on ", summa(summa_2 , y), "km/s")


    
    
