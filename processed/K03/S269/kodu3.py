n = int(input("Sisesta naturaalarv n: "))

r_summa = 0
for i in range(1, n+1):
    r_summa += i**2
summa = 0
for j in range(1, n+1):
    summa += j
    
print(summa**2-r_summa)
    

