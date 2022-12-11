
def summa(esimene, teine):
    c = 299792.458
    nimetaja = (1 + ((esimene * teine)/c**2))
    summa = ((esimene + teine)/nimetaja)
    return summa


esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
    
summa1 = summa(esimene, teine)
summa2 = summa(summa1, kolmas)
summa3 = summa(summa2, neljas)

print("Kiiruste summa on " + str(summa3))