i = 1
n = int(input("Sisesta naturaalarv n: "))
ruutude_summa = 0
summa = 0
summa_ruut = 0

while i <= n:
    ruutude_summa += i ** 2
    summa += i
    i += 1
summa_ruut = summa ** 2
erinevus = summa_ruut - ruutude_summa
print(erinevus)
    