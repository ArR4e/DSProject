def summa(u, v):
    c = 299792.458
    erirelatiivsusteooria = (u + v) / (1 + u*v/(c**2))
    return erirelatiivsusteooria

esimene_keha = float(input("Esimese keha kiirus vaatleja suhtes :" ))
teine_keha = float(input("Teise keha kiirus esimese keha suhtes :" ))
kolmas_keha = float(input("Kolmas keha kiirus teise keha suhtes :" ))
neljas_keha = float(input("Neljas keha kiirus kolmanda keha suhtes :" ))

kõik_kokku = summa(summa(summa(esimene_keha, teine_keha), kolmas_keha), neljas_keha)
print("Kiiruste summa on " + str(kõik_kokku) + " km/s")
