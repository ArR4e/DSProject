n = int(input("Sisesta naturaalarv: "))
summa1 = 0
summa2 = 0

while n > 0:
    summa2 += n
    a = int(n*n)
    summa1 += a
    n -= 1
    
print(summa2 *summa2 - summa1)

