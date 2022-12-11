def transponeeriK(maatriks):
    uus_maatriks = []
    for i in range(len(maatriks)-1,-1,-1):
        uus_index = 0
        for j in range(len(maatriks[0])-1,-1,-1):
            if i == len(maatriks)-1:
                uus_maatriksi_rida = []
                uus_maatriksi_rida.append(maatriks[i][j])
                uus_maatriks.append(uus_maatriksi_rida)
            else:
                uus_maatriks[uus_index].append(maatriks[i][j])
                uus_index = uus_index + 1
    return uus_maatriks