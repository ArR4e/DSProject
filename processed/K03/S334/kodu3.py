n = int(input("Sisesta naturaalarv n: "))
i = 1
summaruut, ruutudesumma = 0, 0
while i <= n:
    summaruut += i
    ruutudesumma = ruutudesumma + (i ** 2)
    i += 1
print(f"Summa ruudu ja ruutude summa erinevus on: {summaruut ** 2 - ruutudesumma}")