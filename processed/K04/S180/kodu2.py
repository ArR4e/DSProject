def summa(u , v):
    return (u + v) / (1 + u * v / c ** 2)

c = 299792.458
u = float(input("Sisesta esimese keha kiirus: "))
v = float(input("Sisesta teise keha kiirus: "))
x = float(input("Sisesta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha kiirus: "))

summa1 = summa(u, v)
summa2 = summa(summa1, x)
summa3 = summa(summa2, y)

print(summa3)