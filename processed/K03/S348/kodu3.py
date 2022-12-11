naturaalarv = int(input("Sisesta naturaalarv: "))
naturaalarv >= 0
ruutude_summa = 0
summa_ruut = 0
n = 0

while n <= naturaalarv:
    ruutude_summa += (n)**2
    summa_ruut += n
    n += 1
summa_ruut = (summa_ruut)**2

print ("Summa ruudu ja ruutude summa erinevus on",summa_ruut-ruutude_summa)
    