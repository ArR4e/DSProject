n = int(input("Sisesta naturaalarv: "))

# esimese kümne naturaalarvu ruutude summa
i = 1
summa = 0

while i <= n:
    summa += i**2
    i = i + 1
summa1 = summa

# esimese kümne naturaalarvu summa ruut
i = 1
summa = 0

while i <= n:
    summa += i
    i= i + 1
summa2 = summa**2

print("Ruutude summa erinevus on " + str(summa2 - summa1) + ".")