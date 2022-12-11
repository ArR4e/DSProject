n = int(input("Sisesta naturaalarv: "))
a = n

summa = 0
summa2 = 0
i = 0

while n > i:
    summa += n
    n -= 1
    
print(i)
print("Naturaalarvu hulgas olevate arvude summa on", summa**2)

while a > i:
    summa2 += a ** 2
    a -= 1
    print(summa2)

print(summa**2 - summa2)
   
    
    

