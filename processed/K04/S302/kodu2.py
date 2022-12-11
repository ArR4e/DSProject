def summa(u, v):
    c = 299792.458
    lopp = 0
    lopp = (u + v) / (1 + ((u * v) / c**2))
    return lopp
esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus vaatleja suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
kokku = summa(summa(summa(esimene, teine), kolmas), neljas)
print("Kiiruste summa on ", str(kokku), " km/s")