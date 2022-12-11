arv = int(input('Sisestage naturaalarv: '))

summa = 0
summa_2 = 0
while arv >= 0:
    summa += arv
    summa_2 += arv**2
    arv -= 1

summa_ruut = summa**2

vastus = summa_ruut - summa_2
print(vastus)

