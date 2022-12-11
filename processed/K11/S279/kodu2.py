def transponeeriK(maatriks):
    ridade_arv = len(maatriks)
    veergude_arv = len(maatriks[0])
    
    transponeeritud_maatriks = []
    for i in range(veergude_arv-1, -1, -1):
        uus_rida = []
        for j in range(ridade_arv-1, -1, -1):
            uus_rida.append(maatriks[j][i])
        transponeeritud_maatriks.append(uus_rida)
        
    return transponeeritud_maatriks