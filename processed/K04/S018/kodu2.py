def summa(u, v):
    c = 299792.458
    kiirus = (u + v)/(1 + u*v/c**2)
    return(kiirus)

k1 = float(input("Kiirus: "))
k2 = float(input("Kiirus: "))
k3 = float(input("Kiirus: "))
k4 = float(input("Kiirus: "))

kiiruste_summa = summa(summa(summa(k1, k2), k3), k4)
print(kiiruste_summa)