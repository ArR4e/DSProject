n = int(input("Sisestage naturaalarv: "))

ruutudesumma = 0
arvudesumma = n

while n >= 1:
    arvuruut = n ** 2
    ruutudesumma = ruutudesumma + arvuruut
    n = n - 1
    arvudesumma = arvudesumma + n


print((arvudesumma ** 2) - ruutudesumma)