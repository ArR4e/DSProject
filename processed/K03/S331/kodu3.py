n = int(input("Sisesta naturaalarv: "))
i = 0
ruutude_summa = 0
j = 0
summa = 0
while i <= n:
    ruutude_summa += i**2
    i += 1
while j <= n:
    summa += j
    j += 1
    summa_ruut = summa**2
erinevus = abs(summa_ruut - ruutude_summa)
print ("Esimese",n ,"naturaalarvu summa ruudu ja ruutude summa erinevus on", erinevus)
