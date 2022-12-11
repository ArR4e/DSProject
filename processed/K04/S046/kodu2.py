def summa(u,v):
    return((u+v)/(1+(u*v)/299792.458**2))
esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus vaatleja suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
neljas = float(input("Neljanda keha kiirus vaatleja suhtes on: "))
print("Kiiruste summa on",summa(summa(summa(esimene, teine),kolmas),neljas),"km/s")