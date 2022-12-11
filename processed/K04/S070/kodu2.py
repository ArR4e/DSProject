import math
def summa(u, v):
    return (u + v) / (1 + (u * v / 299792.458**2))
kokku = 0
kir_1 = float(input("Esimese keha kiirus vaatleja suhtes "))
kir_2 = float(input("Teise keha kiirus esimese keha suhtes "))
kokku = kokku + summa(kir_1, kir_2)
kir_2 = float(input("Kolmanda keha kiirus teise keha suhtes "))
kokku = summa(kokku, kir_2)
kir_2 = float(input("Neljanda keha kiirus kolmanda keha suhtes "))
kokku = summa(kokku, kir_2)
print("Kiiruste summa on", kokku, "km/s")