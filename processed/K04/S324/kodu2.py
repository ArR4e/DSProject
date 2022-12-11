def summa(u, v):
    valem = (u + v) / (1 + ( u * v)/ 299792.458**2)
    return valem

kiirus_1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
kiirus_2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
kiirus_3 = float(input("Kolamanda keha kiirus teise keha suhtes on: "))
kiirus_4 = float(input("Neljanda keha kiirus kolmanda suhtes on: "))
print("Kiiruste summa on ", summa(summa(summa(kiirus_1,kiirus_2),kiirus_3),kiirus_4), "km/s.")



