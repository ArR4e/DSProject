n = int(input("Sisesta üks naturaalarv: "))

i = 1
summa1 = 0
while i <= n:
    summa1 += i**2
    i += 1

i = 1
summa2 = 0
while i <= n:
    summa2 += i
    i += 1
else:
    summa2 = summa2**2

summade_erinevus = summa2 - summa1
print("Naturaalarvude summa ruudu ja ruutude summa erinevus on " + str(summade_erinevus))        