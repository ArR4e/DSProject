natarv = int(input("Sisesta naturaalarv n: "))

summaruut = 0
ruutudesumma = 0
for i in range(1, natarv+1):
    ruutudesumma += i**2
    summaruut += i
vastus = summaruut**2-ruutudesumma
print(vastus)