def summa(u, v):
    c = 299792.458
    summa = (u + v) / (1 + ((u * v) / (c * c)))
    return summa

u = float(input('Esimese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus esimese keha suhtes on: '))
u = summa(u, v)
v = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
u = summa(u, v)
v = float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))

print( 'Kiiruste summa on', summa(u,v) ,'km/s')