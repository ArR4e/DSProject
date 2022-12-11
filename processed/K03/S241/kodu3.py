ruutude_summa = 0
summa_ruut = 0
summa = 0
arv = int(input("Sisesta liidetavate naturaalarvude arv: "))
# ruutude summa     
i=1
while i <= arv:
    ruutude_summa = ruutude_summa + i**2
    i += 1
#summa ruut
j=1
while j <= arv:
    summa = summa + j
    j += 1
summa_ruut = summa**2
print("Esimese ", arv, " naturaalarvu summa ruutude ja ruutude summa erinevus on: ", summa_ruut-ruutude_summa)