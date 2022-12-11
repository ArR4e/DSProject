c = 299792.458 #km/s

def summa(u,v):

    kiirus = (u+v)/(1+(u*v/c**2))
    return kiirus

esimenekiirus = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
teinekiirus = float(input("Sisesta teise keha kiirus vaatleja suhtes: "))
kolmaskiirus = float(input("Sisesta kolmanda keha kiirus vaatleja suhtes: "))
neljaskiirus = float(input("Sisesta neljanda keha kiirus vaatleja suhtes: "))

kiirustesumma = summa(summa(summa(esimenekiirus,teinekiirus),kolmaskiirus),neljaskiirus)
    
print("kiiruste summa on", kiirustesumma)   