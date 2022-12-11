def summa(u, v):
    return (u + v) / (1 + u * v / 299792.458 ** 2)

u = float(input("Sisesta esimene kiirus km/s: "))
v = float(input("Sisesta teine kiirus km/s: "))
x = float(input("Sisesta kolmas kiirus km/s: "))
y = float(input("Sisesta neljas kiirus km/s: "))
kiiruste_summa = summa(summa(summa(u, v), x), y)
print("Kiiruste summa on " + str(kiiruste_summa) + " km/s")