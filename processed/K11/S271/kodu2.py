def transponeeriK(maatriks):
    uus = [[0 for i in range(len(maatriks))] for j in range(len(maatriks[0]))]
    maatriks.reverse()
    for i in range(len(maatriks)):
        for j in range(len(maatriks[0])):
            uus[j][i] = maatriks[i][j]
    uus.reverse()
    return uus         