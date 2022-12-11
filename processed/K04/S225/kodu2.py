def summa(u,v):
    c = 299792.458
    sum = (u + v) / (1 + u*v/(c**2))
    return(sum)

u = float(input('Esimese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus vaatleja suhtes on: '))
x = float(input('Kolmanda keha kiirus vaatleja suhtes on: '))
y = float(input('Neljanda keha kiirus vaatleja suhtes on: '))

sum1 = summa(u,v)
sum2 = summa(sum1, x)
sum3 = summa(sum2, y)

print('Kiiruste summa on', sum3, 'km/s.')