x = int(input('Sisesta naturaalarv:'))
summa = 0
i = 0
ruudud = 0
for i in range(x + 1):
    summa += i
    i += 1
for i in range(x + 1):
    ruudud += i ** 2
    i += 1
print(summa**2 - ruudud)