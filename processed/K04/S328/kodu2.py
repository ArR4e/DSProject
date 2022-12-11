def summa(u, v):
    c = 299792.458
    f = (u + v)/(1 +(u*v/c**2))
    return f

keha_1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
keha_2 = float(input("Teise keha kiirus vaatleja suhtes on: "))
keha_3 = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
keha_4 = float(input("Neljanda keha kiirus vaatleja suhtes on: "))

summa = summa(summa(summa(keha_1, keha_2), keha_3), keha_4)
print("Kiiruste summa on "+ str(summa) + " km/s")
