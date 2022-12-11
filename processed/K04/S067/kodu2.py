def summa(u, v):
    c =  299792.458
    kiirus = (u + v) / (1 + ((u*v) / c ** 2))
    return kiirus

u = float(input('Sisesta kiirus:'))
v = float(input('Sisesta kiirus:'))
x = float(input('Sisesta kiirus:'))
y = float(input('Sisesta kiirus:'))
print(summa(summa(summa(u, v), x), y), 'km/s')
