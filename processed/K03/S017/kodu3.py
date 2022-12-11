#Kirjuta programm, mis leiab esimese n naturaalarvu summa ruudu ja ruutude summa erinevuse.

i = int(input("Palun sisesta üks täisarv: "))

n=0
ruutudesumma=0
summa=0

while not n == i:
    n += 1
    ruutudesumma += n**2
    summa += n

summaruut = summa **2
vastus = abs(summaruut - ruutudesumma)
print(vastus)


    