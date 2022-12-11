
sisend = int(input("Sisestage arv: "))

#summa ruut
summaruut = (sum(range(0, sisend + 1)))**2

#ruutude summa
ruudusumma = 0
for i in range(0, (sisend + 1)):
    ruudusumma += i**2


#print(f"Ruutude summa on {ruudusumma} ja summa ruut on {summaruut}")

print(summaruut-ruudusumma)