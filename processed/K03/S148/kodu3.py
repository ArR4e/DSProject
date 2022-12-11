n = int(input("Sisesta naturaalarvude arv: "))

# Esimese kümne naturaalarvu ruutude summa
i = 1
a = 0

while i <= n:
    a += i**2
    i += 1

# Esimese kümne naturaalarvu summa ruut
j = 1
b = 0

while j <= n:
    b += j
    j += 1
c = b**2

# Summa ruudu ja ruutude summa vahe
print(c - a)