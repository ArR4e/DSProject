arv=int(input("Sisestage arv: "))
a=0
Rsumma=0
summa=0
while a<arv:
    a+=1
    Rsumma+=a**2
b=0
while b<arv:
    b+=1
    summa+=b
summaR=summa**2
#print(summa)
#print(summaR)
#print(Rsumma)
vahe=summaR-Rsumma
print("Erinevus on",vahe)