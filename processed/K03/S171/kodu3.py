n = int(input())
summa1 = 0
summa2 = 0
for x in range (1,n+1):
    summa1 += x**2
for x in range (1,n+1):
    summa2 += x
print (summa2 ** 2 - summa1)
    