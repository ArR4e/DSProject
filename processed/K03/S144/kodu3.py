n = int(input("Sisesta naturaalarv: "))
arv1 = 0
arv2 = 0
summa1 = 0
summa2 = 0

while arv1 <= n:
    summa1 = arv1 ** 2 + summa1
    arv1 += 1

while arv2 <= n:
    summa2 = summa2 + arv2
    arv2 += 1
summa3 = summa2 ** 2

print(summa3 - summa1)