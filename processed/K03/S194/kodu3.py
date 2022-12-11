n = int(input("Naturaalarv: "))

#ruutude summa
rsum = 0
a = 1
while a <= n:
    rsum += a**2
    a += 1

#summa ruut
b = 1
summa = 0
while b <= n:
    summa += b
    b += 1
sumr = summa**2

erinevus = abs(sumr - rsum)
print("esimese " + str(n) + " naturaalarvu ruutude summa: " + str(rsum))
print("esimese", str(n), "naturaalarvu summa ruut:", str(sumr))
print(erinevus)
