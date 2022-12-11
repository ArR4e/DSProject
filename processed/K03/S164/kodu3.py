#EsimeseKümneNaturaalarvudeSumma = (1**2 + 2**2 + "..." + 10**2) = 385

#EsimeseKümneNaturaalarvuSummaRuut = ((1 + 2 + "..." + 10)**2) = 3025
naturaalarv = int(input("Sisesta naturaalarv n: "))
i = 1
ruutude_summa = 0
while i <= naturaalarv:
    
    ruut = i**2
    ruutude_summa = ruut + ruutude_summa
    i += 1
    

naturaalarvude_summa = 0

j = 1
while j <= naturaalarv:
    naturaalarvude_summa = j + naturaalarvude_summa
    j += 1

summa_ruut = naturaalarvude_summa **2


vahe = summa_ruut - ruutude_summa
print(vahe)


#print(naturaalarv)

