n = float(input("Sisesta naturaalarv: "))

i = 0
summa = 0
summa1 = 0
while i <= n:
    summa = i ** 2
    summa1 += int(summa)
    i += 1

j = 0
summa2 = 0
summa3 = 0
while j <= n:
    summa2 = j
    summa3 += summa2
    j += 1

summa3lopp = summa3 ** 2

vastus = summa3lopp - summa1

print("Esimese n naturaalarvu summa ruudu ja ruutude summa vahe on: ", vastus)