c = 299792.458
def summa(a, b):
    return (a + b)/(1 + ((a*b)/c**2))
    
esimene = float(input("Sisestage esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Sisestage teise keha kiirus esimese suhtes on: "))
kolmas = float(input("Sisestage kolmanda keha kiirus teise suhtes on: "))
neljas = float(input("Sisestage neljanda keha kiirus kolmanda suhtes on: "))

vahesumma = summa(esimene, teine)

vahesumma = summa(vahesumma, kolmas)

vahesumma = summa(vahesumma, neljas)

print("Kiiruste summa on ", vahesumma, "km/s")