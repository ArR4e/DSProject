def summa(u, v):
    c = 299792.458
    vastus = (u + v) / (1 + (u*v/c**2))
    return vastus

esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

kogu_summa = summa(summa(summa(esimene, teine), kolmas), neljas)

print(f"Kiiruste summa on {kogu_summa} km/s")