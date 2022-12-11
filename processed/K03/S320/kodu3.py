n = int(input("Sisesta naturaalarv: "))

ruudu_summa = 0
summa_ruut= 0
i = 0

while i <= n:
    ruudu_summa += i**2
    summa_ruut += i
    i += 1
summa_ruut=summa_ruut**2
erinevus= abs(summa_ruut-ruudu_summa)


    
print("esimese", n, "naturaalarvu summa ruudu ja ruutude summa erinevus on", erinevus)