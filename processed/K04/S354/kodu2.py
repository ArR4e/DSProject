c = 299792,458
e = int(input('Esimese keha kiirus vaatleja suhtes on:'))
t = int(input('Teise keha kiirus vaatleja suhtes on:'))
k = int(input('Kolmas keha kiirus vaatleja suhtes on:'))
n = int(input('Neljas keha kiirus vaatleja suhtes on:'))
def summa(x):
    return x = (e + t + k + n)/ (1 + (e * t * k * n) / c ** 2)
print('Kiiruste summa on ', summa(x))