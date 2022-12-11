def summa(u, v):
    c = 299792.458
    return (u + v) / (1 + ((u * v) / c**2))

body1 = float(input('Esimese keha kiirus vaatleja suhtes on: '))
body2 = float(input('Teise keha kiirus vaatleja suhtes on: '))
body3 = float(input('Kolmanda keha kiirus vaatleja suhtes on: '))
body4 = float(input('Neljanda keha kiirus vaatleja suhtes on: '))

print('Kiiruse summa on', summa(summa(summa(body1, body2), body3), body4) , 'km/s')