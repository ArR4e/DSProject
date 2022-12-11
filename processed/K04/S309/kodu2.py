
#defineerime meetodi summa
def summa(u, v):
    c = 299792.458
    return ((u + v) / (1 + ((u*v) / c**2)))

#küsime kasutajalt kiirused
arv1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
arv2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
arv3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
arv4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

#väljastame kiiruste summa
print(summa(summa(summa(arv1, arv2), arv3), arv4))