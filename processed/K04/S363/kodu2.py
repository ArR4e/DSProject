def summa(u,v):
    return (u+v)/(1+(u*v)/299792.458**2)

esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on", summa(neljas, summa(kolmas, summa(teine, esimene))), "km/s")