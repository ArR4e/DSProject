def summa(u, v):
    c2 = 299792.458**2
    kiirus1 = u + v
    kiirus2 = 1 + ((u * v) / c2)
    return kiirus1/kiirus2

kiiruste_summa = summa(float(input("Sisesta esimese keha kiirus: ")), float(input("Sisesta teise keha kiirus: ")))
kiiruste_summa = summa(kiiruste_summa, float(input("Sisesta kolmanda keha kiirus: ")))
kiiruste_summa = summa(kiiruste_summa, float(input("Sisesta neljanda keha kiirus: ")))

print("Kiiruste summa on " + str(kiiruste_summa) + " km/s")