def summa(u, v):
    summa = (u+v)/(1+((u*v)/(299792.458**2)))
    return summa

a = float(input('Esimese keha kiirus vaatleja suhtes on: '))
b = float(input('Teise keha kiirus esimese keha suhtes on: '))
c = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
d = float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))

esimene = summa(a, b)
teine = summa(esimene, c)
kolmas = summa(teine, d)

print('Kiiruste summa on',str(kolmas), 'km/h')