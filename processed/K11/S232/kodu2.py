def transponeeriK(maatriks):
    uus_maatriks = []
    ridade_el_arv = 0
    for rida in maatriks:
        ridade_el_arv = len(rida)
    veeru_el_arv = len(maatriks)
    for i in range(ridade_el_arv - 1, -1, -1):
        uus_veerg = []
        for j in range(veeru_el_arv - 1, -1, -1):
            uus_veerg.append(maatriks[j][i])
        uus_maatriks.append(uus_veerg)
    return(uus_maatriks)
            
transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])