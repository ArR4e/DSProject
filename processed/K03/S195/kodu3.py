n = int(input("Mitu naturaalarvu soovite: "))
i = 1
j = 1
ruutudesumma = 0
summaruut = 0
summa = 0
while i <= n:
    ruutudesumma = ruutudesumma + i ** 2
    i = i + 1
    
    
while j <= n:
    summa = summa + j
    j = j + 1
    
summaruut = summa**2
vahe = summaruut - ruutudesumma
print("Erinevus on", vahe)
    