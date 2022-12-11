
n = int(input("Sisesta naturaalarv: "))
ruutude_summa = 0
loendur = n 
while loendur >= 1:
    ruutude_summa += loendur*loendur
    loendur -= 1
summa = 0
arv = n
while arv >= 1:
    summa += arv
    arv -= 1
summa_ruut = summa*summa

print(summa_ruut - ruutude_summa)