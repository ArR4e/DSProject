u = 0
while u < 2:
    arv = int(input("sisestage üks naturaalarv: "))
    ruut_sum = 0
    esimene_arv = 0
    i = 0
    while i < arv:
        tegur = (esimene_arv + 1) **2
        ruut_sum = ruut_sum + tegur
        i = i + 1
        esimene_arv = esimene_arv + 1
    summa = (((2 + (arv - 1)) / 2) * arv) **2
    print("sinu naturaalarvu ruutude summa ja summa ruudu vahe on " + str(summa - ruut_sum))
     