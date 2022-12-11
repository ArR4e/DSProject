valguskiirus = 299792.458 #km/s

def summa(kiirus1, kiirus2):
    return (kiirus1 + kiirus2) / (1 + ((kiirus1 * kiirus2) / (valguskiirus**2)))

keha1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
keha2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
keha3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
keha4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

kokku = summa(keha4, summa(keha3, summa(keha1, keha2)))

print("Kiiruste summa on " + str(kokku) + " km/s")