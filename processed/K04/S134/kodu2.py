u = float(input("Esimese keha kiirus vaatleja suhtes on : "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))


def summa(u, v):
    c = 299792.458
    s = (u + v)/(((u*v)/c**2)+1)
    return(s)
s = summa(u, v)
s2 = summa(s, x)
s3 = summa(s2, y)
print("Kiiruste summa on", s3, "km/s")

                      