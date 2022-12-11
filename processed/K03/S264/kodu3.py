n = int(input("Sisestage naturaalarv: "))

i = 1
ruutude_summa = 0

while i <= n:
    ruut = i * i
    ruutude_summa += ruut
    i = i + 1

i = 1
summa = 0

while i <= n:
    summa += i
    summa_ruut = summa*summa
    i = i + 1
vahe = summa_ruut - ruutude_summa
print("Esimese", n, "naturaalarvu summa ruudu", summa_ruut, "ja ruutude summa", ruutude_summa, "vahe on", vahe, ".")