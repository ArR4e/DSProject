def transponeeriK(maatriks):
    lopp = []
    for i in range(len(maatriks[0])-1,-1, -1):
        ajutine = []
        for j in range(len(maatriks)-1, -1, -1):
            ajutine.append(maatriks[j][i])
        lopp.append(ajutine)
    return lopp