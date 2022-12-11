n = int(input("Sisesta naturaalarv: "))

summa = 0
i = summa_järk = 1
ruut_summa = 0
j = ruut_järk = 1

while i <= n:
    summa += i ** 2
    i += 1
while j <= n:
    ruut_summa += j
    j += 1
ruut_summa **= 2
vahe = ruut_summa - summa
print(vahe)