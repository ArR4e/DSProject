c = 299792.458

def summa(u,v):
    return (u + v) / (1 + u*v/c**2)

u = float(input("Sisesta esimese keha kiirus: "))
v = float(input("Sisesta teise keha kiirus: "))
x = float(input("Sisesta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha kiirus: "))

kiirus1 = summa(u,v)
kiirus2 = summa(kiirus1,x)
kiirus3 = summa(kiirus2,y)


print("Kiiruste summa on " + str(kiirus3) + " km/s")