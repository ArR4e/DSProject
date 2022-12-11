n = int(input("Sisesta naturaalarv: "))
summa = 0
ruutudesumma = 0
while n > 0:
    summa += n
    ruutudesumma += n*n
    n -= 1
print (summa**2-ruutudesumma)