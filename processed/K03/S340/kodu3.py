import numpy as np

n = int(input("Palun sisestage naturaalarv: "))
list_n = range(1,n+1)
summaruut = sum(list_n)**2
n_naturaalarvu_ruutude_summa = sum(np.square(list_n))
ruutude_summa_erinevus = summaruut - n_naturaalarvu_ruutude_summa
print("Esimese " + str(n) + " naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(ruutude_summa_erinevus) + ".")