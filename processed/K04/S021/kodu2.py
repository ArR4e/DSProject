def summa(u, v):
    c=299792.458
    esimene = ((u+v)/(1+((u*v)/(c**2))))
    return esimene

kiirus1 = float(input("Sisestage esimese keha kiirus vaatleja suhtes: "))

kiirus2 = float(input("Sisestage teise keha kiirus esimese keha suhtes: "))

tulemus1 = summa(kiirus1, kiirus2)

kiirus3 = float(input("Sisestage kolmanda keha kiirus teise keha suhtes: "))

tulemus2 = summa(tulemus1, kiirus3)

kiirus4 = float(input("Neljanda keha kiirus kolmanda keha suhtes: "))

tulemus3 = summa(tulemus2, kiirus4)

print("Kiiruste summa on" , tulemus3 , "km/s")