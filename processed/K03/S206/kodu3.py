n = int(input("Sisesta naturaalarv: "))

i = 1
rsumma = 0
summa = 0
while i <= n:
    rsumma += i**2
    summa += i
    i += 1
sruut = summa**2

vahe = sruut - rsumma

print("Esimese ", n, "naturaalarvu summa ruudu ja ruutude summa vahe on ", vahe)