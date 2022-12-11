i = int(input("Sisesta naturaal arv: "))

ruutude_summa = 0
summa_ruut = 0

while i > 0:
    ruutude_summa = ruutude_summa + i ** 2
    summa_ruut = summa_ruut + i
    i = i - 1

print("Summa ruudu ja ruutude summa: ", (summa_ruut) ** 2 - ruutude_summa)