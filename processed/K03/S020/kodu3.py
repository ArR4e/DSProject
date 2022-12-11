'''
Esimese kümne naturaalarvu ruutude summa on

12 + 22 + ... + 102 = 385

Esimese kümne naturaalarvu summa ruut on

(1 + 2 + ... + 10)2 = 552 = 3025

Seega esimese kümne naturaalarvu summa ruudu ja ruutude summa erinevus on 3025 - 385 = 2640.

Kirjuta programm, mis leiab esimese n naturaalarvu summa ruudu ja ruutude summa erinevuse.

Automaatkontroll. Programm peab kasutaja käest küsima naturaalarvu n ja kuvama ekraanile õige vastuse.


'''
n = int(input("Sisesta mitme naturaalarvu kohta vastust soovid:"))
p = int(n)
summa=0
summa3=0
summa2=0
summa4=0
#Ülihalb kood, aga nii magamata, et aju ei tööta, aga toimib vist
for i in range(1, n+1):
    summa = summa + (i*i)

summa2=0
for s in range(1, p+1):
    summa2 = summa2 + s
summa3=summa2*summa2

summa4=summa3-summa
print(summa4)