# Kirjuta programm, mis leiab esimese n naturaalarvu summa ruudu ja
# ruutude summa erinevuse. 

naturaalArv = int(input('sisestage naturaalarv '))

summaRuut = 0
ruutudeSumma = 0
n = naturaalArv

# liidab naturaalarvud kokku ja pärast tsüklit leiab summa ruudu.
# Tsüklis leiab ka ruutude summa
while n > 0:
    summaRuut = summaRuut + n
    ruutudeSumma = ruutudeSumma + n**2
    n -= 1
summaRuut = summaRuut**2

erinevus = summaRuut - ruutudeSumma

print('esimese', naturaalArv, 'naturaalarvu summa ruudu ja ruutude summa erinevus on', erinevus)

