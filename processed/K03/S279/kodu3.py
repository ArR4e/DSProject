naturaalarv = int(input("Sisesta naturaalarv: "))

summa = 0
i = 0
while i <= naturaalarv:
    summa = summa + i
    i = i + 1
summa_ruut = summa**2

ruutude_summa = 0
j = 0
while j <= naturaalarv:
    ruutude_summa = ruutude_summa + j**2
    j = j + 1
    
print("Esimese", naturaalarv, "naturaalarvu summa ruudu ja ruutude summa erinevus on", summa_ruut-ruutude_summa)
    

