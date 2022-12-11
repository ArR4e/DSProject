c =  299792.458
u = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
v = float(input("Sisesta teise keha kiirus esimese keha suhtes: "))
x = float(input("Sisesta kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Sisesta neljanda keha kiirus kolmanda keha suhtes: "))
def summa(u, v):
    return (u + v)/(1 + u*v/c**2)
esimesekahesumma = summa(u, v)
def summa(esimesekahesumma, x):
    return (esimesekahesumma + x)/(1 + esimesekahesumma*x/c**2)
kolmandaga = summa(esimesekahesumma, x)
def summa(kolmandaga, y):
    return (kolmandaga + y)/(1 + kolmandaga*y/c**2)
kogusumma = summa(kolmandaga, y)
print("Kiiruste summa on :", kogusumma, "km/s")


