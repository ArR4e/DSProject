n = int(input("Kirjuta siia üks naturaalarv: "))

summa = 0
i = 0
ruut_summa = 0
o = 0

while i <= n:
    summa += i
    i += 1
summa_ruut = summa**2
print(n, "esimese n naturaalarvu summa ruut on", summa_ruut)

while o <= n:
    ruut_summa += o**2
    o += 1
print(n, "esimese n naturaalarvu ruutude summa on", ruut_summa)

vastus = summa_ruut - ruut_summa
print("Summa ruudu ja ruutude summa erinevus on: ", vastus)
