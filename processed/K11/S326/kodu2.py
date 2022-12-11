def transponeeriK(maatriks):
    uus_maatriks = []
    for j in range(len(maatriks[0])):
        uus_rida = []
        for i in range(len(maatriks)):
            uus_rida.append(maatriks[i][j])
        uus_maatriks.append(uus_rida)
    return uus_maatriks