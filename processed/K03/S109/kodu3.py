n = int(input("Sisesta naturaalarv: "))
i = 1
summa = 0
while i <= n:
    summa += i
    i += 1

j = 1
summa2 = 0
while j <= n:
    summa2 = summa2 + j*j
    j = j + 1

print(summa**2 - summa2)
