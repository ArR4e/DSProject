n = int(input("Sisesta naturaalarv: "))
i = 1 #loendur
#tekitan kaks summat
summa = 0
ruutudesumma = 0
while i <= n:
    summa += i
    ruutudesumma += i**2
    i += 1

summaruut = summa**2
erinevus = summaruut - ruutudesumma
print(erinevus)