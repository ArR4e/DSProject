n = int(input("Sisestage naturaalarv: "))

ruutude_summa = 0
for i in range(n):
    ruutude_summa += (i + 1) ** 2

summa_ruut = sum(range(n + 1)) ** 2

print(summa_ruut - ruutude_summa)