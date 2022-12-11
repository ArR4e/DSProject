
arv=int(input("Sisesta arv: "))
i=1
ruutude_summa=0
summa_ruut=0
while i<=abs(arv):
    ruutude_summa = ruutude_summa + i**2 
    i=i+1
    
arvude_summa=0
n=1
while n<=abs(arv):
    arvude_summa = arvude_summa + n
    n=n+1 

summa_ruut=arvude_summa**2
print(summa_ruut-ruutude_summa)
   