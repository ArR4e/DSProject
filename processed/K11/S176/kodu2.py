def transponeeriK(maatriks):
    transponeeritud = []
    
    for i in range(len(maatriks[0]) -1, -1, -1):
        elemendid = []
        for j in range(len(maatriks) - 1, -1, -1):
            elemendid += [maatriks[j][i]]
        transponeeritud += [elemendid]
    return transponeeritud


