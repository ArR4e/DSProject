#Esimese kümne naturaalarvu ruutude summa on
#1^2 + 2^2 + ... + 10^2 = 385

#Esimese kümne naturaalarvu summa ruut on
#(1 + 2 + ... + 10)^2 = 552 = 3025

#Seega esimese kümne naturaalarvu summa ruudu
#ja ruutude summa erinevus on 3025 - 385 = 2640.

#Kirjuta programm, mis leiab esimese n naturaalarvu summa ruudu ja
#ruutude summa erinevuse.

n = int(input("Sisesta naturaalarv: "))
i= 1
ruudud= 0
summa= 0

while i <= n:
    lüli_1= (1*i)**2
    ruudud += lüli_1
    i +=1
# tsükkel liidab muutujale ruudud ühe võrra suureneva arvu ruudu juurde
#tsükkel lõppeb kui seda on läbitud kasutaja poolt soovitud korrad

print('Ruutude summa on: '+ str(ruudud))

i-=n
#i tuleb uuesti ära nullida, et samas algorütm toimiks ka hiljem

while i <= n:
    lüli_2= (1*i)
    summa += lüli_2
    i +=1
summa_ruut= summa**2

#tsükkel liidab muutujale summa järjest suurenevaid arve kasutaja sisestatud korrad
# seejärel võtab saadud summa ruutu

print('Summa ruut on: '+ str(summa_ruut))

erinevus= summa_ruut- ruudud

print('Esimese',n , 'naturaalarvu summa ruudu ja ruudude summa erinevus on:', erinevus)
