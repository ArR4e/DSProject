n = int(input("Sisesta naturaalarv: "))

summa1 = 0
summa = 0
i = 0

while i <= n:
    summa += i
    i += 1

while n > 0:
    summa1 = summa1 + (n * n)
    n = n - 1

print ((summa ** 2) - summa1)

