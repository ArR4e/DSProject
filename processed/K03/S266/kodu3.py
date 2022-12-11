#ruudud

n = int(input("Sisestage naturaalarv: "))

summa = 0
ruutude_summa = 0
i = 1
while i <= n:
    ruutude_summa += i**2
    summa += i
    i += 1

summa_ruut = summa**2
vahe = summa_ruut - ruutude_summa

print(vahe)