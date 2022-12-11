def summa(u, v):
    return(u + v / (1 + u * v / 299792.458 ** 2))

u = float((input("siseta esimene number: ")))
v = float((input("sisesta teine number: ")))


print(summa(u, v))
