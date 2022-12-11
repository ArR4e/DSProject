naturaalarv = int(input("Sisesta palun esimene n naturaalarv: "))

esimese_n_naturaalarvu_summa_ruut = str(int((naturaalarv * (naturaalarv + 1) / 2) * (naturaalarv * (naturaalarv + 1) / 2))) 
y = int(esimese_n_naturaalarvu_summa_ruut)
esimese_n_naturaalarvu_ruutude_summa = str(int((naturaalarv * (naturaalarv + 1) * (2 * naturaalarv + 1)) / 6))
x = int(esimese_n_naturaalarvu_ruutude_summa)

erinevus = y - x
print ("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(erinevus) + ".")