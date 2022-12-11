n=int(input("arv"))
ruutude_summa=0
for a in range(n+1):
    ruutude_summa+=a**2
summa_ruut=0
for a in range(n+1):
    summa_ruut+=a
summa_ruut=summa_ruut**2
if summa_ruut>=ruutude_summa:
    print(summa_ruut-ruutude_summa)
else: print(summa_ruut-ruutude_summa*-1)