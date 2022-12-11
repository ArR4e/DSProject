#Ruudud ning nende summad tsükli abil
n = i = int(input("Sisesta naturaalarv: "))

summa = 0
#tühjad muutujad, millega saab opereerida
b=0
p=0
#funktsionaalne muutuja, millega saab tõsta järjestust 10-ni.
while b <= n:
    summa += b**2
    b += 1
    
print(summa)

summa2=0

while p <= i:
    summa2 += p
    p += 1
print(summa2)

erinevus=summa2**2-summa
print(erinevus)
