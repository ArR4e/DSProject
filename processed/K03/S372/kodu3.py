naturaalarv = int(input("Sisestage naturaalarv: "))
i = 0
ruutude_summa = 0
while i <= naturaalarv:
    ruutude_summa = ruutude_summa + i**2
    i += 1

k = 0
summa = 0
while k <= naturaalarv:
    summa += k
    k += 1
summa_ruut = summa**2
print(summa_ruut - ruutude_summa)