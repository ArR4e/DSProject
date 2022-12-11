x = int(input("Sisesta naturaalarv: "))

#ruutude summa
n = 1
summa = 0
while n <= x:
    summa += n**2
    n = n + 1

#summa ruut
n = 1
summa_ruut = 0
while n <= x:
    summa_ruut = summa_ruut + n
    n = n + 1
summa_2 = int(summa_ruut)**2

a = int(summa_2 - summa)
print("Summa ruudu ja ruutude summa erinevus on " + str(summa_2) + " - " + str(summa) + " = " + str(a))