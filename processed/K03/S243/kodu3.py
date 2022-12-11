#Ruudud
n=int(input("Sisesta naturaalarv: "))
if n<0:
    print("Peab olema positiivne!")
    n=int(input("Sisesta naturaalarv: "))
i=1
ruutude_summa=0
while i<=n:
    ruutude_summa+=i**2
    i+=1
    
u=1
summa=0
while u<=n:
    summa+=u
    u+=1

summa_ruut=summa**2
erinevus=summa_ruut-ruutude_summa
print(erinevus)