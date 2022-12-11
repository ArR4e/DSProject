import math
n = int(input("Sisestage n väärtus "))
i = 0
j = 0
k = 0
while i != n: 
    j = j + (i + 1)*(i + 1) #Arvutan naturaalarvude ruutude summa
    k = k + i + 1 #Arvutan naturaalarvude summa
    i = i + 1 #Valin järgmise naturaalarvu
k = k * k  #Tõstan saadud naturaalarvude summa ruutu
print(abs(j - k))
