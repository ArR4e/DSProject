n = int(input('Vali naturaalarv n: '))

#ruutude summa
r_summa = 0
for i in range(n):
    r_summa += (i + 1)**2 #i + 1 sest range algab 0-st
    
#summa ruut
summa = 0
for i in range(n):
    summa += (i + 1) #i + 1 sest range algab 0-st

summa_r = summa**2

vahe = summa_r - r_summa
print(vahe)