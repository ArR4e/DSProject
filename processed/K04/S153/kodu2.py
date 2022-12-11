c = 299792458
u = float(input("Esimese keha kiirus vaatleja suhtes: "))
v = float(input("Teise keha kiirus esimese keha suhtes: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes: "))

def summa(u, v):
    a = (u+v)/(1 + (u*v)/c**2)
    return a
a = summa(u, v)


def summa(a, x):
    b = (a+x)/(1 + (a*x)/c**2)
    return b
b = summa(a, x)


def summa(b, y):
    d = (b+y)/(1 + (b*y)/c**2)
    return d
d = summa(b, y)

print("Kiiruste summa on " + str(d) + " km/s")





