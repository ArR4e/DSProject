arv = int(input("Sisestage naturaalarv n: "))

summa=0
ruut=0
for i in range(arv+1):
    summa += i**2
    ruut += i
ruut = ruut**2

erinevus = ruut-summa

print(erinevus)