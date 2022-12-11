n = int(input("Palun sisesta naturaalarv: "))
ruutude_summa = (round)(n * (n + 1) * (2 * n + 1) / 6)
summa_ruut = (round)(n * (n + 1) / 2) ** 2
print(summa_ruut - ruutude_summa)
