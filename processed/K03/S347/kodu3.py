a = int(input("Sisesta naturaalarv: "))
summaruut = 0
ruutudesumma = 0
for i in range(a):
     summaruut += i + 1
for i in range(a):
    ruutudesumma += (i + 1)**2
print("Summa ruudu ja ruutude summa vahe on:" + str(summaruut**2 - ruutudesumma))
