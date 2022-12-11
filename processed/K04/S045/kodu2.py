def summa(u, v):
    #u - esimese keha suhtes
    #v = teise keha suhtes
    c = 299792.458 #valguse kiirus, km/s
    return (u + v) / (1 + ((u*v)/c**2))
u = float(input('Esimese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus esimese keha suhtes on: '))
x = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
y = float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))

vastus = summa(summa(summa(u, v), x), y)
print('Kiiruste summa on', vastus, 'km/s')