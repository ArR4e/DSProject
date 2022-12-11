def transponeeriK(sisend):
    x = len(sisend)
    ridade_arv = x-1
    y = len(sisend[0])
    veergude_arv = y-1
    loendus_veerud = 0
    algne_maatriks = []
    maatriks = []
    while veergude_arv > -1:
        while ridade_arv > -1:
            algne_maatriks.append(sisend[ridade_arv][loendus_veerud])
            ridade_arv -=1
        maatriks.append(algne_maatriks)
        algne_maatriks = []
        ridade_arv = x-1
        loendus_veerud +=1
        veergude_arv -=1
    lõplik_maatriks = maatriks[::-1]
    return(lõplik_maatriks)