def summa(u, v):
    c = 299792.458
    kiiruste_summa = (u + v) / (1 + u * v / c **2)
    return kiiruste_summa

esimene_keha = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine_keha = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas_keha = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas_keha = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
print("Kiiruste summa on " + str(summa(summa(summa(esimene_keha, teine_keha), kolmas_keha), neljas_keha)) + " km/s.")
    
