import math

def summa(a, b):
    return (a + b) / (1 + (a*b / pow(299792.458, 2)))

esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

kiiruste_summa = summa(esimene, teine)
kiiruste_summa = summa(kiiruste_summa, kolmas)
kiiruste_summa = summa(kiiruste_summa, neljas)

print("Kiiruste summa on ", kiiruste_summa, " km/s")