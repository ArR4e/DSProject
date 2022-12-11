n = int(input("Sisestage naturaalarv n: "))
ruutude_summa = 0
summa_ruut = 0

for i in range(1, n+1):
    ruutude_summa+=i*i
    summa_ruut+=i
    
summa_ruut = summa_ruut*summa_ruut

print(ruutude_summa, summa_ruut)

print(summa_ruut-ruutude_summa)