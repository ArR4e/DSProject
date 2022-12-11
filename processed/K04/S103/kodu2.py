kiirus1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
kiirus2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
kiirus3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
kiirus4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

def summa(u, v):
    c = 299792.458
    return (u + v)/(1+(u*v)/c**2)

summa1 = summa(kiirus1, kiirus2)
summa2 = summa(summa1, kiirus3)
summa_kokku = summa(summa2, kiirus4)
print("Kiiruste summa on",summa_kokku, "km/s")

