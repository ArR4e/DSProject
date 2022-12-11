n = int(input("Sisesta naturaalarv: "))

ruutude_summa = 0
summa = 0
i = 0

while i <= n:
    ruutude_summa += i**2
    summa += i
    i += 1

summa_ruut = summa**2
vahe = summa_ruut - ruutude_summa

print(vahe)
