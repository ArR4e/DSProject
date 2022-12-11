n = int(input("Sisesta naturaalarv: "))

korrutis = 0
i = 0

while i <= n:
    korrutis += i * i
    i += 1

summa = 0
i = 0

while i <= n:
    summa += i
    i += 1
summa_ruut = summa * summa

vahe = summa_ruut - korrutis

print(vahe)