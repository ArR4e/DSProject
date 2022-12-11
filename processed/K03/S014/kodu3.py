arv=int(input("Sisesta naturaalarv (s.o positiivne täisarv): "))
i=0
summa=0
ruudu_summa=0

while i<=arv:
    summa+=i
    ruudu_summa+=i**2
    i+=1
    
summa_ruut=summa**2
vahe=summa_ruut-ruudu_summa

print("Esimese "+str(arv)+" naturaalarvu summa ruudu ("+str(summa_ruut)+") erinevus nende samade arvude ruutude summast ("+str(ruudu_summa)+") on "+str(vahe)+".")
