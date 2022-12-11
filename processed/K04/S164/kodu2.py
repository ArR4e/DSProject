
c = 299792.458

def summa(u,v):
    return (u + v) / (1 + ((u * v) / c**2))


esimese_keha_kiirus = float(input("Esimese keha kiirus vaatleja suhtes on :"))
teise_keha_kiirus = float(input("Teise keha kiirus esimese keha suhtes on :"))
kolmanda_keha_kiirus = float(input("Kolmanda keha kiirus teise keha suhtes on :"))
neljanda_keha_kiirus = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

esimese_ja_teise_kiiruse_summa = summa(esimese_keha_kiirus, teise_keha_kiirus)
kolmanda_kiiruse_summa = summa(esimese_ja_teise_kiiruse_summa, kolmanda_keha_kiirus)
neljanda_kiiruse_summa = summa(kolmanda_kiiruse_summa, neljanda_keha_kiirus)

print("Kiiruste summa on " + str(neljanda_kiiruse_summa) + " km/s")












#input("Kolmanda keha kiirus teise keha suhtes on :")
#input("Neljanda keha kiirus kolmanda keha suhtes on: ")
