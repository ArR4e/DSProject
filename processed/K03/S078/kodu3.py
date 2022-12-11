n = int(input("Kui palju naturaalarvu?: "))
summa1 = summa2 = 0
i = 1
while i <= n:
    summa1 += i**2
    summa2 += i
    i += 1
print("Seega esimese kümne naturaalarvu summa ruudu ja ruutude summa erinevus on", summa2**2 - summa1)