n = int(input("Sisestage naturaalarv: "))
summa1 = 0
summa2 = 0
m = n
while n > 0:
    summa1 += n
    n -= 1

while m > 0:
    summa2+= m**2
    m -= 1

print(summa1**2 - summa2)
    
    








