n = int(input("Sisestage naturaalarv "))
i = 1
x = 1
ruutude_summa = 0

while i <= n :
    x = i ** 2
    ruutude_summa += x
    i+= 1

a = 1
summa = 0
while a <= n :
    summa += a
    a += 1

summa_ruut = (summa**2)
erinevus = summa_ruut - ruutude_summa

print(erinevus)