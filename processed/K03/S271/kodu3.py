arv = int(input('sisesta arv'))

ruutude_summa =0
summa_ruut = 0
i = 1
while i <= arv:
    ruutude_summa += i**2
    summa_ruut += i
    i +=1
summa_ruut = summa_ruut**2
print(summa_ruut - ruutude_summa)