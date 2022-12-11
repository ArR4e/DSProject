nat_arv=input("Sisesta naturaalarv: ")
n=int(nat_arv)

summa=0
i=0
while i<=n:
    summa +=i
    i+=1
summa_ruut=summa**2

u=0
summa_=0
while u<=n:
    summa_ +=u**2
    u+=1
    
vahe= summa_ruut-summa_
print(summa_)
print(summa_ruut)
print(vahe)