n = int(input("Mitu arvu? "))

i = 1
summa1 = 0
summa2 = 0
while i <= n:
    summa1 += i**2
    summa2 += i
    i += 1

summa2 = summa2 ** 2
vahe = summa2 - summa1
print(vahe)