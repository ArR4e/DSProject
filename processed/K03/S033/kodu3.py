n = int(input("Sisesta naturaalarv: "))
ruut_summa = 0
i = n
while i > 0:
    ruut_summa += i ** 2
    i -= 1
#print(ruut_summa)

summa = 0
while n > 0:
    summa += n
    n -= 1
summa_ruut = summa ** 2
#print(summa_ruut)
print(summa_ruut - ruut_summa)