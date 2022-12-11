n = int(input("Palun sisesta naturaalarv: "))
m = n
summa = 0

while n > 0:
    summa = summa + n**2
    n -= 1
    
ruut = 0

while m > 0:
    ruut = ruut + m
    m -= 1
    
ruut = ruut ** 2

print("Vahe on", ruut - summa)