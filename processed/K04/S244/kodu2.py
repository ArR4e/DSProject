def summa(u, v):
    c = 299792.458
    return((u+v)/(1+(u*v/(c**2))))


samm1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
samm2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
samm3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
samm4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

summa1 = summa(samm1, samm2)
summa2 = summa(summa1, samm3)
summa3 = summa(summa2, samm4)
print("Kiiruste summa on " + str(summa3) + " km/s")