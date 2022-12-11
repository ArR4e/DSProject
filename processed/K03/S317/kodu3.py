a = input("Sisesta naturaalarv n: ")
n = int(a)
summa = 0
i = 1
while i <= n:
    summa += i*i
    i += 1
summa1 = 0
n = int(a)
i = 1
while i <= n:
    summa1 += i
    i += 1
summa2 = summa1**2
vahe = summa2-summa
print("n naturaalarvu summa ruudu ja ruutude summa vahe on", vahe)
