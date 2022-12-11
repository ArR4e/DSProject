def summa(a,d):
    c = 299792.458
    a = float(a)
    d = float(d)
    kiirus = (a + d)/(1+((a*d)/c**2))
    return(kiirus)
    
    
kiirus1 = input("Sisestage keha kiirus:")
kiirus2 = input("Sisestage keha kiirus:")
kiirus3 = input("Sisestage keha kiirus:")
kiirus4 = input("Sisestage keha kiirus:")

print("Esimese keha kiirus vaatleja suhtes on:",(kiirus1))
print("Teise keha kiirus esimese keha suhtes on:", (kiirus2))
print("Kolmanda keha kiirus teise keha suhtes on:", (kiirus3))
print("Neljanda keha kiirus kolmanda keha suhtes on:",(kiirus4))


summa1 = summa(kiirus1, kiirus2)
summa2 = summa(summa1, kiirus3)
summa3 = summa(summa2, kiirus4)

print("Kiiruste summa on: ", summa3, "km/s")

    
    
    