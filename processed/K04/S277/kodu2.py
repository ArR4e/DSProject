c = 299792.458

def summa(u, v):
    summa1 = (u + v) / (1 + (u * v / c ** 2))
    summa2 = (summa1 + x) / (1 + (summa1 * x / c ** 2))
    summa3 = (summa2 + y) / (1 + (summa2 * y / c ** 2))
    return summa3


print('Sisesta kiirused teisendatuna km/s')
u = float(input('Esimese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus esimese keha suhtes on: '))
x = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
y = float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))


print('Kiiruste summa on', summa(u, v), 'km/s')
