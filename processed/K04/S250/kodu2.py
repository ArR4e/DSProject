c = 299792.458

def summa(a,b):
    return ((a+b)/(1+((a*b)/(c**2))))

u = float(input())
print('Esimese keha kiirus vaatleja suhtes on:', u)
v = float(input())
print('Esimese keha kiirus vaatleja suhtes on:', v)
x = float(input())
print('Esimese keha kiirus vaatleja suhtes on:', x)
y = float(input())
print('Esimese keha kiirus vaatleja suhtes on:', y)
print('Kiiruste summa on', (summa(summa(summa(u,v),x),y)), 'km/s')