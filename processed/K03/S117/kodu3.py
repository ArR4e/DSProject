# alustasin 13.09.2021 (23:07)
narv = int(input('Sisestage n naturaalarvu: '))

while narv < 0:
    narv = int(input('Sisestage n naturaalarvu: '))

summa = 0
summaruut = 0
ruutudesumma = 0

if narv >= 0:
    while summa < narv:
        summa += 1
        summaruut += summa #esimese n naturaalarvu summa ruut
        ruutudesumma += summa**2 #esimese n naturaalarvu ruutude summa
    print('Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on ' + str(summaruut**2-ruutudesumma))