# 2. Einsteini erirelatiivsusteooria / RP
c = 299792.458

def summa(u, v):
    return float((u + v) / (1 + ((u * v) / c ** 2)))

esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teiste keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on " + str(summa(summa(summa(esimene,teine), kolmas), neljas)) + " km/s")