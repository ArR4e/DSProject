n = int(input("Sisestage naturaalarv: "))
i = 1
n2 = n
summa1 = 0
summa2 = 0

while n > 0:
    summa1 += n ** 2
    n -= 1

while n2 > 0:
    summa2 += n2
    n2 -= 1
summa2 = summa2 ** 2

erinevus = summa2-summa1

if erinevus < 0:
    erinevus = -erinevus
    
print(erinevus)