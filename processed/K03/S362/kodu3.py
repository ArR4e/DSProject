from math import *

n=int(input("Sisestage naturaalarv: "))
naturaalarvude_ruutude_summa=0
naturaalarvude_summa=0

while n>0:
    naturaalarvude_ruutude_summa=naturaalarvude_ruutude_summa+n**2
    naturaalarvude_summa=naturaalarvude_summa + n
    n=n-1

naturaalarvude_summa_ruut=naturaalarvude_summa**2
erinevus=naturaalarvude_summa_ruut-naturaalarvude_ruutude_summa

    
print(erinevus)

