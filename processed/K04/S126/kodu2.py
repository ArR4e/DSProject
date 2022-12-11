u = float(input("Esimese keha kiirus vaatleja suhtes on : "))
v = float(input("Teise keha kiirus vaatleja suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
def summa(u, v):
    valguskiirus = 299792.458
    esimene = ( (u+v) / (1 + ( (u*v) / valguskiirus**2) ))
    teine = ( ( esimene + x) / (1 + ( (esimene * x) / valguskiirus**2) ))
    kolmas = ( ( teine + y) / (1 + ( (teine * y) / valguskiirus ** 2) ))
    print("Kiiruste summa on " + str(kolmas) + "km/s.")
summa(u, v)