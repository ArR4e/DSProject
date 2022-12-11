def summa(u, v):
    return (u+v)/(1+((u*v)/299792.458**2))
u = int(input("Sisesta esimese keha kiirus: "))
v = int(input("Sisesta teise keha kiirus: "))
x = int(input("Sisesta kolmanda keha kiirus: "))
y = int(input("Sisesta neljanda keha kiirus: "))
print("kiiruste summa on: ", summa(summa(summa(u, v), x), y), "km/s")