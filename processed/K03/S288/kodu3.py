n = int(input('Sisestage naturaalarv: '))
ruutude_summa = 0
summa_ruut = 0

for x in range(1, n + 1):
    ruutude_summa = ruutude_summa + (x * x)
    
for y in range(1, n + 1):
    summa_ruut = y + summa_ruut

tulemus = summa_ruut ** 2 - ruutude_summa

print(tulemus)