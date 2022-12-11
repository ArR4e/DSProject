n = int(input("Sisesta, mitut naturaalarvu vaaldeldakse: "))

summa = 0
i = 0

while i <= n:
    summa = summa + i*i
    i= i+1

summa2= 0
i=0
while i <= n:
    summa2 = summa2 + i
    i = i +1

vahe= summa2**2 - summa
print(n, "naturaalarvu summa ruudu ja ruutude summa erinevus on", vahe)