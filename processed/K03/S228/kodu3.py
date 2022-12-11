arv = int(input("Sisesta naturaalarv n: "))
summa = 0
ruutude_summa = 0

if arv >= 0:
    while arv >= 0:
        summa += arv
        summa_ruut = summa**2
        ruutude_summa += arv**2
        arv -= 1
        erinevus = summa_ruut - ruutude_summa
    print("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(erinevus) + ".")

else:
    print("Viga. Proovi uuesti.")