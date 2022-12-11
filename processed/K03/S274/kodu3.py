natarv = int(input("Sisesta naturaalarv: "))

i1 = 1
summa1 = 0
while i1 <= natarv:
    summa1 += i1
    i1 += 1
    summaruut = summa1 ** 2

i2 = 1
ruutsumma = 0
while i2 <= natarv:
    ruutsumma += i2 ** 2
    i2 += 1

tulem = summaruut - ruutsumma
print("Ühest sisestatud naturaalarvuni arvutatud summa ruudu ja nende arvude ruutude summa erinevus on", tulem, ".")
