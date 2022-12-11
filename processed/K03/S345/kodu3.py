n = int(input("Sisestage naturaalarv: "))
ruutudesumma = 0
summa = 0

while n > 0:
    ruutudesumma += n**2
    summa += n
    n -= 1

summaruut = summa**2
vahe = summaruut - ruutudesumma

print(vahe)