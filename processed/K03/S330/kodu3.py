n = int(input("Sisestage naturaalarv: "))
a = 0
ruutude_summa = 0
summa_ruut = 0
while a <= n:
    ruutude_summa += a ** 2
    summa_ruut += a
    a += 1
summa_ruut = summa_ruut ** 2
vahe = summa_ruut - ruutude_summa
print("Esimese", n, "naturaalarvu summa ruudu ja ruutude summa vahe on", vahe)