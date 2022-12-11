def summa(u, v):
    vastus = (u + v) / (1 + (u * v / c ** 2))
    return(float(vastus))
c = 299792.458

u = float(input('Sisesta esimese keha kiirus vaatleja suhtes: '))
v = float(input('Sisesta teise keha kiirus esimese keha suhtes: '))
x = float(input('Sisesta kolmanda keha kiirus teise keha suhtes: '))
y = float(input('Sisesta neljanda keha kiirus kolmanda keha suhtes: '))

esimene_summa = summa(u, v)
teine_summa = summa(esimene_summa, x)
kogu_summa = summa(teine_summa, y)
print("Kiiruste summa on ", kogu_summa, "km/s")