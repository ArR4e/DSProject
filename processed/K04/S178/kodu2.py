def summa(u,v):
    c = float(299792.458)
    algus1 = u * v / (c ** 2)
    keskmine1 = 1 + algus1
    lopp1 = float((u + v) / keskmine1)
    return lopp1


u = float(input("Sisesta esimese keha kiirus km/s: "))
v = float(input("Sisesta teise keha kiirus km/s: "))
n = float(input("Sisesta kolmanda keha kiirus km/s: "))
l = float(input("Sisesta neljand keha kiirus km/s: "))

print("Kiiruste summa on", ((summa(summa(summa(u,v),n),l))), "km/s")
