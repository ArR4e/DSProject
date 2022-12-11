n = int(input('Sisestage naturaalarv: '))
summa_ruut = 0
ruutude_summa = 0
while n > 0:
    ruutude_summa += n**2
    summa_ruut += n
    n -= 1
summa_ruut = summa_ruut ** 2
erinevus = summa_ruut - ruutude_summa
print('Naturaalarvu summa ruut ja ruutude summa erinevus on ' + str(erinevus) + '.')


    
    
