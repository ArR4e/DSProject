def transponeeriK(maatriks):
    transponeeritud_maatriks = []
    veergude_arv = len(maatriks[0])
    ridade_arv = len(maatriks)
    for veerg in range(veergude_arv - 1, -1, -1):
        uus_rida = []
        for rida in range(ridade_arv - 1, -1, -1):
            uus_rida.append(maatriks[rida][veerg])
        transponeeritud_maatriks.append(uus_rida)
    return transponeeritud_maatriks
        
print(transponeeriK([[4, 31, 67, 99]]))
