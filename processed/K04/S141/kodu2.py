def summa(u, v):
    c = 299792.458
    return (u + v)/(1 + (u * v)/c**2)

keha_1 = float(input("Esimese keha kiirus vaatleja suhtes on:"))
keha_2 = float(input("Teise keha kiirus esimese keha suhtes on:"))
keha_3 = float(input("Kolmanda keha kiirus teise keha suhtes on:"))
keha_4 =  float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))

#print(summa(keha_1, keha_2))
#print(summa(summa(keha_1, keha_2), keha_3))
print(summa(summa(summa(keha_1, keha_2), keha_3), keha_4))