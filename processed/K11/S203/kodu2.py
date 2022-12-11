def transponeeriK(maatriks):
    uus_maatriks = []
    try:
        veergude_arv = len(maatriks[0])
        ridade_arv = len(maatriks)
        for v in range(veergude_arv-1, -1, -1):
            uus_rida = []
            for r in range(ridade_arv-1, -1, -1):
                uus_rida.append(maatriks[r][v])
            uus_maatriks.append(uus_rida)
    except:
        ridade_arv = len(maatriks)
        uus_maatriks = list(reversed(maatriks))
    return uus_maatriks
