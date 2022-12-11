def summa(u, v):
    u = ((u + v) / (1 + (u * v / 299792.458**2)))
    return(u)

u = float(input('Sisesta esimene number: '))
v = float(input('Sisesta teine number: '))
u = summa(u, v)
v = float(input('Sisesta kolmas number: '))
u = summa(u, v)
v = float(input('Sisesta neljas number: '))
print(summa(u, v))