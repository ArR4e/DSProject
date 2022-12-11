esimene = float(input("Sisestage esimese keha kiirus vaatleja suhtes: "))
teine = float(input("Sisestage teise keha kiirus esimese keha suhtes: "))
kolmas= float(input("Sisestage kolmanda keha kiirus teise keha suhtes: "))
neljas= float(input("Sisestage neljanda keha kiirus kolmanda keha suhtes: "))
def summa(u, v):
    c = 299792.458
    return (u + v) / (1 + (u * v) / c**2)
summa2 = summa(esimene,teine)
summa3 = summa(summa2,kolmas)
summa_kokku = summa(summa3,neljas)
print("Kiiruste summa on " + str(summa_kokku) + " km/s")