n = abs(int(input("Sisesta naturaalarv n: ")))
ruutudesumma = 0
summa = 0
summaruut = 0
erinevus = 0
for i in range (1, n+1):
    ruutudesumma += i**2
    summa += i
    summaruut = (summa **2)
    erinevus = (summaruut - ruutudesumma)
print("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on: ", erinevus)