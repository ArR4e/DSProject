naturaalarv = int(input("Sisesta naturaalarv n: "))

i = 0
summa = 0
while i <= naturaalarv:
    summa += i
    i = i + 1
    summa_ruut = summa * summa
i = 0
ruutude_summa = 0
while i <= naturaalarv:
    ruutude_summa += i * i
    i = i + 1
print("Naturaalarvu", naturaalarv, "summa ruudu ja ruutude summa erinevus on", summa_ruut - ruutude_summa)