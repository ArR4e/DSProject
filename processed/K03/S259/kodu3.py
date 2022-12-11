n = int(input("Sisesta naturaalarv: "))

summa = 0
summa2 = 0
i = 0

while i <= n:
    summa += i
    summa2 += i**2
    i += 1
    
print((summa**2) - summa2)