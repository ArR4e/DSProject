def summa(u, v):
    return (u + v) / (1 + u * v  / (299792.458 * 299792.458))

print(summa(100000, 200000))

u = float(input("Esimene kiirus: "))
v = float(input("Teine kiirus: "))
x = float(input("Kolmas kiirus: "))
y = float(input("Neljas kiirus: "))

summa1 = summa(u, v)

summa2 = summa(summa1, x)

summa3 = summa(summa2, y)

print(summa3)

    
    
