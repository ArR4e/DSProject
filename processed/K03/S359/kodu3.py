n= int(input("Sisesta mitut naturaalarvu soovid: "))
nsumma=0
ruutsumma=0
i=0
while i <= n:
    nsumma += i**2
    i += 1
i=0
while i <= n:
    ruutsumma += i
    i += 1
ruutsumma= ruutsumma**2

vastus= ruutsumma - nsumma
print(n, "esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on: ", vastus)