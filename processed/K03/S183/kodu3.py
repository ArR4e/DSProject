n = int(input("Sisesta naturaalarv: "))
i = 0
summa = 0
ruut = 0

while i <= n:
    summa += i
    ruut += i**2
    i += 1
    
print((summa**2) - ruut)