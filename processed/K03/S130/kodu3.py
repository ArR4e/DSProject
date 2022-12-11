n = int(input("Sisesta naturaalarv: "))
i = 0
summa = 0

while i <= n:
    summa += i**2
    i += 1
print("esimese", n, "naturaalarvu ruutude summa on", summa)
i = 0
summa1 = 0
while i <= n:
    summa1 += i
    i += 1
summa2 = summa1**2
print("esimese", n, "naturaalarvu summa ruut on", summa2)
print("Esimese", n, "naturaalarvu summa ruudu ja ruutude summa erinevus on", summa2 - summa)