naturaalarv = int(input("Sisestage naturaalarv n: "))

i = 1
naturaalarvu_ruutude_summa = 0

while i <= naturaalarv:
    naturaalarv_ruudus = i ** 2
    naturaalarvu_ruutude_summa += naturaalarv_ruudus
    i += 1
    
j = 1
naturaalarvu_summa = 0
while j <= naturaalarv:
    naturaalarvu_summa += j
    j += 1
    naturaalarvu_summa_ruut = naturaalarvu_summa ** 2
    
print("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(naturaalarvu_summa_ruut - naturaalarvu_ruutude_summa) + ".")