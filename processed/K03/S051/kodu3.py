arv = int(input("Sisesta naturaalarv: "))
i = 0
summa_ruut = 0
ruutude_summa = 0

while i < arv:
    i += 1
    summa_ruut += i
    ruutude_summa += i**2

summa_ruut **= 2

print(summa_ruut - ruutude_summa)    