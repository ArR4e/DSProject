naturaalarv = int(input("Sisesta naturaalarv: "))
ruutsumma = 0
summaruut = 0
i = 0

while i <= naturaalarv:
    ruutsumma += (i)**2
    summaruut += i 
    i += 1

summaruut = summaruut**2

print("Summa ruudu ja ruutude summa erinevus on",summaruut-ruutsumma)


