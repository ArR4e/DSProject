n = int(input("Sisestage naturaalarv: "))
summaruut = 0
ruutudesumma = 0
for i in range(n+1):
    summaruut = summaruut + i
    ruutudesumma = ruutudesumma + (i*i)
print("Naturaalarvu summa ruudu ja ruutude summa erinevus on:",((summaruut*summaruut))-ruutudesumma)