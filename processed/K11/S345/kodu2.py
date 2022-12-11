def transponeeriK(maatriks):
    transponeeritud_maatriks = []
    maatriks2 = maatriks.reverse()
    
    for el in maatriks:
        el = el.reverse()

    for j in range(len(maatriks[0])):
        uus_rida = []
        for i in range(len(maatriks)):
            uus_rida.append(maatriks[i][j])
        transponeeritud_maatriks.append(uus_rida)
        
    return transponeeritud_maatriks