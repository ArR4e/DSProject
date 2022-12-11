def summa(u,v):
    c = 299792.458
    tehe = (u+v)/(1+((u*v)/c**2))
    return tehe
esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print(summa(neljas,summa(kolmas,summa(esimene,teine))))