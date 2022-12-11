def transponeeriK(maatriks):
    suurus = len(maatriks[0])
    uus_maatriks = []
    for el in range(suurus):
        uus_maatriks.append([0]*len(maatriks))
    for i, rida in enumerate(maatriks):
        for j, number in enumerate(rida):
            uus_maatriks[-1*j-1][-1*i-1] = number
    return uus_maatriks