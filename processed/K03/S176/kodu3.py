n = int(input("Sisesta naturaalarv: "))
i = 1
ruutude_summa = 0
summa = 0
while i <= n:
    ruutude_summa += (i ** 2)
    summa += i
    summa_ruut = summa ** 2
    i = i + 1
vahe = summa_ruut - ruutude_summa
print("Esimese ", n, "naturaalarvu summa ruudu ja ruutude summa vahe on ", vahe)