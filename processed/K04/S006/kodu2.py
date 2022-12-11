
u = float(input("Sisesta esimese keha kiirus: "))
v = float(input("Sisesta teise keha kiirus esimese suhtes: "))
x = float(input("Sisesta kolmanda keha kiirus teise suhtes: "))
y = float(input("Sisesta neljanda keha kiirus kolmanda suhtes: "))

def summa(u, v):
    c = 299792.458
    summa = (u + v)/(1 + u*v/c**2)
    return summa

xkiirus = summa(summa(u, v), x)
ykiirus = summa(xkiirus, y)
print("Kiiruste summa on ", ykiirus, " km/s.")