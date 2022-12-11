# 3. Ruudud
# Esimese kümne naturaalarvu ruutude summa on
# 12 + 22 + ... + 102 = 385

# Esimese kümne naturaalarvu summa ruut on
# (1 + 2 + ... + 10)2 = 552 = 3025

# Seega esimese kümne naturaalarvu summa ruudu ja ruutude summa erinevus on 3025 - 385 = 2640.
# Kirjuta programm, mis leiab esimese n naturaalarvu summa ruudu ja ruutude summa erinevuse.
# Automaatkontroll. Programm peab kasutaja käest küsima naturaalarvu n ja kuvama ekraanile õige vastuse.

n = int(input("Sisesta naturaalarv n: "))
i = 0
summa_ruut = 0
ruutude_summa = 0

while i <= n:
    ruutude_summa += i**2
    summa_ruut += i
    i += 1
summa_ruut = summa_ruut**2
vahe = summa_ruut - ruutude_summa

print(vahe)
