naturaalarv = int(input("Sisesta naturaalarv: "))
ruutude_summa = 0
summa_ruut = 0
i=0
for s in range(1, naturaalarv+1):
    ruutude_summa = ruutude_summa + (s*s)
    
while i <= naturaalarv:
    summa_ruut += i
    i += 1
vahe = summa_ruut*summa_ruut - ruutude_summa

print("Ruutude summa on " + str(ruutude_summa) + ".")
print("Summa ruut on " + str(summa_ruut*summa_ruut) + ".")
print("Summa ruudu ja ruutude summa vahe on " + str(vahe) + ".")
