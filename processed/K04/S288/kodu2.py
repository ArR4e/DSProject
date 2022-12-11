def summa(u, v):
    return (u + v) / (1 + (u * v) / c**2)

c = 299792.458
u = float(input('Sisestage esimese keha kiirus vaatleja suhtes: '))
v = float(input('Sisestage teise keha kiirus esimese keha suhtes: '))
x = float(input('Sisestage kolmanda keha kiirus teise keha suhtes: '))
y = float(input('Sisestage neljanda keha kiirus kolmanda keha suhtes: '))

summa1 = summa(u, v)
summa2 = summa(summa1, x)
summa3 = summa(summa2, y)

print('Kiiruste summa on', summa3,'km/s.')