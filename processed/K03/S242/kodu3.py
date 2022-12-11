n = int(input("Sisesta naturaalarv:"))
i = 0
ruutude_summa = 0
summa_ruut = 0
while i <= n:
    ruutude_summa = ruutude_summa + i**2
    summa_ruut += i
    i += 1

summa_ruut = summa_ruut**2
print(summa_ruut - ruutude_summa)