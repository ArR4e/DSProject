n = int(input('Anna mulle naturaalarv: '))

summa = 0
i = 1
ruut = 0

while n >= i:
    summa = summa + i
    i = i + 1

while n > 0:
    ruut = n * n + ruut
    n -= 1

print(summa ** 2 - ruut)