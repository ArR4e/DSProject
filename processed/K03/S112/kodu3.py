n = int(input("Sisesta naturaalarv:"))

ruutude_summa = 0
i = 0

while i <= n:
    ruutude_summa += i**2
    i += 1

summa = 0
i = 0

while i <= n:
    summa += i
    i += 1

summa_ruut = summa**2

print(summa_ruut - ruutude_summa)