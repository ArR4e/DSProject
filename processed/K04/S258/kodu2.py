c=299792.458
def summa(u,v):
    return (u+v)/(1+(u*v)/c**2)
uks = float(input("Esimese keha kiirus vaatleja suhtes on: "))
kaks = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolm = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neli = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
print("Kiiruste summa on "+str(summa(summa(summa(uks,kaks),kolm),neli))+" km/s")




