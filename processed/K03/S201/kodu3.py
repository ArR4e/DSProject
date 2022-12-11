a = int(input("Sisesta naturaalarv:"))
i = 1
summa1 = 0
while i <= a:
    summa1 += i*i
    i +=1
n = 1
summa2 = 0
while n <= a:
    summa2 += n
    n +=1
print(summa2**2 - summa1)

