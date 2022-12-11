arv = int(input("Sisesta naturaalarv: "))
summa = 0
summa2 = 0
i = 0
while arv > i:
    i += 1
    summa += (i**2)
    summa2 += i

print((summa2**2)-summa)
