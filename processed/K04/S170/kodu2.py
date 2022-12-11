from math import *
c = 299792.458

esimene = float(input("Palun sisestage esimese keha kiirus: "))
teine = float(input("Palun sisestage teise keha kiirus: "))
kolmas = float(input("Palun sisestage kolmanda keha kiirus: "))
neljas = float(input("Palun sisestage neljanda keha kiirus: "))


def summa(x, y):
    valem = (x + y)/(1 + ((x*y)/c**2))
    return valem


es = summa(esimene, teine)
tei = summa(es, kolmas)
kol = summa(tei, neljas)

print("Kiiruste summa on:", kol)