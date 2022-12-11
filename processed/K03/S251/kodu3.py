n = int(input("Sisestage naturaalarv: "))
ruutude_summa = 0
summa_ruut = 0

for i in range(n+1):
    ruutude_summa += i**2
    summa_ruut += i

summa_ruut = summa_ruut**2

print("Esimese " + str(n) + " naturaalarvu summa ruudu vahe ruutude summaga on " + str(summa_ruut - ruutude_summa))