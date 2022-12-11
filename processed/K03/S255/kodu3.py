n = int(input('Sisesta naturaalarv: '))
ruutude_summa = 0
summa_ruut = 0

for i in range(n):
    i += 1
    summa_ruut += i

for i in range(n):
    i += 1
    ruutude_summa += i**2
    
print(f"Naturaalarvu summa ruudu ja ruutude summa vahe on {summa_ruut**2 - ruutude_summa}")