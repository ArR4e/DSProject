c = 299792.458 #km1/s


def summa(u, v):
    n = (u+v)/(1+(u*v/(c**2)))
    s = (n+x)/(1+(n*x/(c**2)))
    value = (s+y)/(1+(s*y/(c**2)))
    return value + n + s + u

u = float(input("esimene kiirus "))
v = float(input("teine kiirus (esimese suhtes) "))
x = float(input("kolmas kiirus (teise suhtes) "))
y = float(input("neljas kiirus (kolmanda suhtes) "))
print("kiiruste summa on " + str(summa(u, v)) + " m/s")