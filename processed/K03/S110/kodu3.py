arv = int(input('Sisesta naturaalarv: '))

i = 0
ruutude_summa = 0
summa_ruut = 0
while i < arv:
    
    #arv = arv + i
    i += 1
    
    ruut = (i)**2
    ruutude_summa += ruut
    
    summa_ruut += i
vahe = summa_ruut**2 - ruutude_summa

print(vahe)