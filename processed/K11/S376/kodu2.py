def transponeeriK(maatriks):
    read = len(maatriks)
    veerud = len(maatriks[0])

    uus = [[0 for i in range(read)] for j in range(veerud)]

    maatriks.reverse()

    for i in range(read):
        for j in range(veerud):
            uus[j][i] = maatriks[i][j]
            
    uus.reverse()
    return uus