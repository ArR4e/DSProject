n = int(input("Sisesta naturaalarv: "))

summa = 0
i = 0
ruutude_summa = 0
l = 0

while i <= n:
    summa += i
    i += 1
summa_ruut = summa ** 2
#print(summa_ruut)

while l <= n:
    ruutude_summa += l**2
    l += 1
#print(ruutudesumma)
    
print(summa_ruut - ruutude_summa)


