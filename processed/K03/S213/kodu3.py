piir = int(input("Sisesta naturaalarv: "))

#naturaalarvu ruutude summa
ruutude_summa = 0
i = 1
while i <= piir:
    ruutude_summa += pow(i, 2)
    i+=1

#naturaalarvu summa ruut
summa_ruut = 0
i = 1
while i <= piir:
    summa_ruut += i
    i+=1
summa_ruut = pow(summa_ruut, 2)

print(summa_ruut - ruutude_summa)