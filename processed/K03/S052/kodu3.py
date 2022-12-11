n = int(input("Sisesta mingi naturaalarv: "))
ruudu_summa = 0
summa = 0
i = 1

while i <= n:
    ruudu_summa += i**2
    summa += i
    i += 1

summa_ruut = summa**2
erinevus = abs(summa_ruut - ruudu_summa)

print("Tulemuste erinevus on: " + str(erinevus) + ".")