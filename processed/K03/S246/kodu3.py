n = int(input("Sisestage naturaalarv: "))

ruutude_summa = 0
i = 0

while i <= n:
    ruutude_summa += i ** 2
    i += 1


summa = 0
j = 0

while j <= n:
    summa += j
    j += 1
summa_ruut = summa ** 2


print(summa_ruut - ruutude_summa)