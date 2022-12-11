arv = int(input("Sisesta naturaalarv: "))
summa = 0
summa2 = 0
m = arv
n = arv

while m > 0:
    summa += m
    m -= 1
sr = summa ** 2

while n > 0:
    summa2 += n ** 2
    n -= 1
rs = summa2

print(sr - rs)