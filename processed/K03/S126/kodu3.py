n = int(input("Sisestage üks naturaalarv "))
r = 1
m = 1

ruutude_summa = 0
summa_ruut = 0

#ruutude_summa
while r <= n:
    ruutude_summa += r**2
    r += 1
    
#summa_ruut
while m <= n:
    summa_ruut += m
    m += 1
    
summa_ruut = summa_ruut**2 
se=summa_ruut-ruutude_summa

print(se)
