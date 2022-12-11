n = int(input("Sisestage naturaalarvu: "))
i = 1
summa1 = 0
summa2 = 0

while i <= n:
    summa1 += i
    a = i**2
    summa2 += a
    i += 1
    
summa1 = summa1 ** 2
vahe = summa1 - summa2
print("Vastus on", vahe)