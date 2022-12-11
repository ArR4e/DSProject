def transponeeriK(maatriks):
    uus_maatriks = []
    ridade_arv = 0
    veergude_arv = 0
    for a in maatriks:
        ridade_arv += 1
        if ridade_arv == 1:
            for b in a:
                veergude_arv += 1
    for i in range(veergude_arv - 1,-1,-1):
        järjend_elementidele = []
        for j in range(ridade_arv - 1,-1,-1):
            järjend_elementidele.append(maatriks[j][i])
        uus_maatriks.append(järjend_elementidele)
    return uus_maatriks
