from math import*

n=int(input("Sisesta naturaalarv n:"))
summaruut=0
ruutudesumma=0
a=1
while a<=n:
    ruutudesumma=ruutudesumma+a**2
    a+=1
a=1
while a<=n:
    summaruut=summaruut+a
    a+=1
summaruut=summaruut**2
print("Naturaalarvude 1-n summa ruudu ja ruutude summa erinevus on", round(summaruut-ruutudesumma, 0), ".")