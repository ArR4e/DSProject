#Esimese kümne naturaalarvu ruutude summa on
#12 + 22 + ... + 102 = 385
#Esimese kümne naturaalarvu summa ruut on
#(1 + 2 + ... + 10)2 = 552 = 3025
#Seega esimese kümne naturaalarvu summa ruudu ja ruutude summa erinevus on 3025 - 385 = 2640.
#Kirjuta programm, mis leiab esimese n naturaalarvu summa ruudu ja ruutude summa erinevuse.
#Automaatkontroll. Programm peab kasutaja käest küsima naturaalarvu n ja kuvama ekraanile õige vastuse.
n = int(input("Sisestage naturaalarv: "))

i = 1
summa = 0

while i <= n:
    summa += i**2
    i += 1


o = 1
x = 0

while o <= n:
    x += o
    o += 1



print(x**2 - summa)
    