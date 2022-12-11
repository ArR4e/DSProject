i=0
ruutude_summa = 0
summa = 0
naturaalarv=int(input("Sisesta naturaalarv: "))
while i <= naturaalarv:
    ruut = i ** 2
    ruutude_summa = ruut + ruutude_summa
    summa += i
    i += 1
summa_ruut = summa**2
tulemus=summa_ruut-ruutude_summa
print("Summa ruudu ja ruutude summa vahe on " + str(tulemus) + ".")