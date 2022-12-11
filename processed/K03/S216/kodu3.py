arv = int(input("Sisesta naturaalarv: "))
arv1 = 0
ruutudesumma = 0
summa = 0
while arv1 < arv:
    arv1 = arv1 + 1
    summa += arv1
    ruut = arv1**2
    ruutudesumma = ruutudesumma + ruut
summaruut = summa**2
print(summaruut)
print(ruutudesumma)

erinevus = summaruut - ruutudesumma
print(erinevus)

