def summa(u, v):
    c = 299792.458
    u = float(u)
    v = float(v)
    murd = u*v/c**2
    lugeja = u + v
    nimetaja = 1 + murd
    kiirus = lugeja / nimetaja
    return kiirus

text = '. keha kiirus vaatleja suhtes on: '
u = input('1'+ text)
v = input('2'+ text)
x = input('3'+ text)
y = input('4'+ text)

vastus = summa(summa(summa(u, v), x), y)
print("Kiiruste summa on", vastus, 'km/s')