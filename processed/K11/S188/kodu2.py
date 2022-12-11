def transponeeriK(maatriks):
    maatriks_t = []
    rida = []
    for j in range(len(maatriks[0]) - 1, -1, -1):
        for i in range(len(maatriks) - 1, -1, -1):
            rida += [maatriks[i][j]]
        maatriks_t += [rida]
        rida =[]
    return maatriks_t