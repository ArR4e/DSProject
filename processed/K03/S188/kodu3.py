n = float(input("Sisesta naturaalarv: "))
summa = 0
ruutude_summa = 0
i = 1
while i <= n:
    summa += i
    ruutude_summa += i*i
    i += 1

print("Summa ruudu ja ruutude summa erinevus on", summa * summa - ruutude_summa)