def summa(u, v):
    summa = (u + v) / (1 + (u * v) / 299792.458**2)
    return summa

esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine   = float(input("Teise keha kiirus vaatleja suhtes on: "))
kolmas  = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
neljas  = float(input("Neljanda keha kiirus vaatleja suhtes on: "))

kokku = summa(summa(summa(esimene, teine), kolmas), neljas)
print("Kiiruste summa on ", kokku, " km/s.")