n = int(input('Sisestage arv: '))
i = 1
korrutis = 0
summa = (i + n) * 0.5 * n
while i <= n:
    #1^2 + 2^2 + ... n^2
    korrutis += i * i
    i += 1


    
vastus = -1 * (korrutis - summa ** 2)
print(summa)
print(korrutis)


print(vastus)
