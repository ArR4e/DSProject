n = int(input("Sisesta mitme esimese naturaalarvu summade ruudu ja ruutude summa vahet leida: "))

ruutude_summa = 0
i = n
while i > 0:
    ruutude_summa += i**2
    i -= 1

j = n

summade_ruut = 0
while j > 0:
    summade_ruut += j
    j -= 1
summade_ruut = summade_ruut ** 2

print(summade_ruut - ruutude_summa)