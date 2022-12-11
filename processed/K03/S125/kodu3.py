n = int(input("Sisetage naturaalarv: "))

summa1 = 0 #naturaalarvude summa
i = 0

#arvutab naturaalarvude summat
while i <= n:
    summa1 += i
    i += 1
    
summa_ruut = summa1**2

summa2 = 0 #naturaalarvude ruudute summa
i2 = 0
#arvutab naturaalarvude ruudute summat
while i2 <= n:
    summa2 += i2**2
    i2 += 1

erinevus = summa_ruut - summa2

print("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on:", erinevus)
