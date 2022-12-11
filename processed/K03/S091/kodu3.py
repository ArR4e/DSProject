number = int(input("Sisestage number: "))
ruudud = 0
summa = 0

for i in range(1, number+1):
    ruudud += i**2
    
for i in range(1, number+1):
    summa += i
    
summa_ruut = summa**2
vastus = summa_ruut - ruudud
print(vastus)

    
