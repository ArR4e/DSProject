n = int(input("sisesta naturaalarv :"))

ruutsum = 0
summa = 0

while n > 0:
    ruutsum = ruutsum + n**2
    summa += n
    n -= 1
    
sumruut = summa**2

print(sumruut-ruutsum)
