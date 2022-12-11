# Ruudud

n = int(input("Sisesta mingi positiivne täisarv: "))
i = 0
while n <= 0 and i < 5:
    n = int(input("Sisestage mingi positiivne täisarv:"))
    i += 1

if i == 5:
    print("Te ei ole ikka suutnud sisestada positiivset täisarvu...")
else:
    ruutude_summa = 0
    summa_ruut = 0
    i = 1

    while i != n + 1:
        ruutude_summa += i**2
        summa_ruut += i
        i += 1

    vahe = summa_ruut**2 - ruutude_summa

    print("summa ruudu ja ruutude summa erinevus on: " + str(vahe))
