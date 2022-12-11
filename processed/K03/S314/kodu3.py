n = int(input("Sisesta naturaalarv: "))
a = 1
b = 1
ruutude_summa = 0
summa = 0
while a <= n:
    ruutude_summa += a**2
    a += 1
while b <= n:
    summa += b
    b += 1
summa_ruut = summa**2
print(summa_ruut - ruutude_summa)
