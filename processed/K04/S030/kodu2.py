u=float(input("Sisesta u: "))
v=float(input("Sisesta v: "))
x=float(input("Sisesta x: "))
y=float(input("Sisesta y: "))
def summaA(u):
    return ((u)/(1+299792.458**2))
def summaB(summaA, v):
    return ((summaA+v)/(1+((summaA*v)/299792.458**2)))
def summaC(summaB, x):
    return ((summaB+x)/(1+((summaB*x)/299792.458**2)))
def summaD(summaC, y):
    return ((summaC+y)/(1+((summaC*y)/299792.458**2)))

print('Esimese keha kiirus vaatleja suhtes on: ', summaA(u))
print('Teise keha kiirus esimese keha suhtes on: ', summaB(summaA(u), v))
print('Kolmanda keha kiirus teise keha suhtes on: ', summaC(summaB(summaA(u), v), x))
print('Neljanda keha kiirus kolmanda keha suhtes on: ', summaD(summaC(summaB(summaA(u), v), x), y))
print('Kiiruste summa on:', summaA(u)+summaB(summaA(u), v)+
      summaC(summaB(summaA(u), v), x)+summaD(summaC(summaB(summaA(u), v), x), y), "km/s.")