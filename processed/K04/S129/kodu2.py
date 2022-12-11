
c = 299792.458
def summa(u,v):
    return (u + v) / (1 + (u*v/c**2))



esimene = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda suhtes on: "))

print("Kiiruste summa on", summa(summa(summa(esimene,teine), kolmas), neljas))
