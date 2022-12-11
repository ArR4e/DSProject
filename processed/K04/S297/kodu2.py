u = int(input('Sisestage esimene kiirus (km/s):'))
v = int(input('Sisestage teine kiirus (km/s):'))
x = int(input('Sisestage kolmas kiirus (km/s):'))
y = int(input('Sisestage neljas kiirus (km/s):'))
c = 299792.458

def summa1(u, v) :
    return (u + v) / (1 + ((u * v) / c**2))
a = summa1(u, v)

def summa2(x, a) :
    return (x + a) / (1 + ((x * a) / c**2))
b = summa2(x, a)

def summa(y, b) :
    return (y + b) / (1 + ((y * b) / c**2))


print(summa(y, b))