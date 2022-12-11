arv = int(input("Sisesta naturaalarv: "))
i = 0
ruutude_summa = 0
summa_ruut = 0

while i < arv:
    i += 1
    ruutude_summa += i**2
    summa_ruut += i

summa_ruut = summa_ruut **2
erinevus = summa_ruut - ruutude_summa
print("Summa ruudu ja ruutude summa erinevus on :" + str(erinevus)) 