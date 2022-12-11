naturaalarv = int(input("Sisestage naturaalarv: "))
#Esimeste n naturaalarvu ruutude summa
a=1
ruutude_summa=0
while a <= naturaalarv:
    arvu_ruut=a**2
    ruutude_summa += arvu_ruut
    a=a+1

#Esimeste naturaalarvude summa ruut
a=1
arvu_summa=0
while a <= naturaalarv:
    arvu_summa += a
    a=a+1
arvu_summa_ruut=(arvu_summa)**2

arvude_vahe=(arvu_summa_ruut) - (ruutude_summa)

print("Esimese kümne naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(arvude_vahe))