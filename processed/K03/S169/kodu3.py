arv = int(input("Sisesta naturaalarv: "))
ruutudesumma = 0
summa = 0
for a in range(arv+1):
    ruutudesumma += a**2
    summa += a
    
summaruut = summa**2

print("Summma ruudu ja ruutude summa erinevus on",summaruut-ruutudesumma)