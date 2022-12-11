n=int(input("Sisesta naturaalarv: "))
i=1
summa=0
while i<=n:
    summa+=i
    i+=1
    summa_ruut=summa*summa
j=0
summa=0
while j<=n:
    summa=summa+j*j
    j+=1
    ruutude_summa=summa

erinevus=summa_ruut-summa
print(n," esimese naturaalarvu summa ruudu ja ruutude summa erinevus on ",erinevus)