n = int(input("Sisesta naturaalarv: "))
ruutudesumma = 0
summaruut = 0
while n > 0:
    ruutudesumma = ruutudesumma + (n ** 2)
    summaruut = summaruut + n
    n -= 1
summaruut = summaruut ** 2
erinevus = summaruut - ruutudesumma
print("Erinevus ruutude summa ja summa ruudu vahel on " + str(erinevus) + ".")