u = float(input("Sisestage esimese keha kiirus vaatleja suhtes: "))
v = float(input("Sisestage teise keha kiirus esimese keha suhtes: "))
x = float(input("Sisestage kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Sisestage neljanda keha kiirus kolmanda keha suhtes: "))
c = 299792.458



def summa(u,v):
    while True:
        vastus = (u + v) / (1 + (u * v) / c**2)
        return vastus
    
esimene = summa(u,v)
teine = summa(esimene, x)
kolmas = summa(teine, y)

print(f"Kiiruste summa on {round(kolmas, 2)}")