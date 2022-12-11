u = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
v = float(input("Sisesta teise keha kiirus esimese keha suhtes: "))
w = float(input("Sisesta kolmanda keha kiirus teise keha suhtes: "))
x = float(input("Sisesta neljanda keha kiirus kolmanda keha suhtes: "))
c = 299792.458
def summa1(u,v):
    return (u+v)/(1 + (u*v / c**2))
def summa2(u,w):
    u = summa1(u,v)
    return (u+w)/(1 + (u*w / c**2))
def summa3(u,x):
    u = summa2(u,w)
    return (u+x)/(1 + (u*x / c**2))
print("Kiiruste summaks on", float(summa3(u,x)), "km/s")

    