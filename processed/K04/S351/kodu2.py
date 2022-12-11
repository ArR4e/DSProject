
def summa(u, v):
    c=299792.458
    kiiruste_summa=(u+v)/(1+(u*v/(c**2)))
    return kiiruste_summa


esimese_keha_kiirus=float(input("Esimese keha kiirus vaatleja suhtes on: "))
teise_keha_kiirus=float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmanda_keha_kiirus=float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljanda_keha_kiirus=float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
    

print("Kiiruste summa on " + str(summa(summa(summa(esimese_keha_kiirus, teise_keha_kiirus), kolmanda_keha_kiirus), neljanda_keha_kiirus)))