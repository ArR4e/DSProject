n= int(input("Sisesta naturaalarv: "))
summa = 0
i = 1
while i <= n:
    summa += i
    i += 1
summaruut = summa**2

ruutudesumma = 0
j = 1
while j <= n:
    ruutudesumma += j ** 2
    j += 1
erinevus = summaruut - ruutudesumma
print("Summa ruudu ja ruutude summa erinevus on: " + str(erinevus))
    
    