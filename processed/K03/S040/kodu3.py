a = int(input("Sisesta naturaalarv: "))
summa = 0
summa2 = 0
i = 0
while i <= a:
    summa += i
    i += 1

while i <= a:
    summa2 += i*i
    i += 1
x = summa ** 2 - summa2
print("Naturaalarvu summa ruudu ja ruutude summa erinevus on: " + str(x))