def summa(u, v):
    c = 299792.458
    return((float(u) + float(v))/(1 + (float(u) * float(v))/ c ** 2))

a = float(input("Sisestage esimene kiirus"))
b = float(input("Sisestage teine kiirus"))
d = float(input("Sisestage kolmas kiirus"))
e = float(input("Sisestage neljas kiirus"))


x1 = summa(a,b)
x2 = summa(x1, d)
x3 = summa(x2, e)

print("Kiiruste summa on", str(x3), "km/s")
