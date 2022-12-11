def transponeeriK(maatriks):
    jõr =[]
    for i in range(len(maatriks[0])-1, -1 ,-1):
        m = []
        for j in range(len(maatriks)-1, -1, -1):
            m += [maatriks[j][i]]
        jõr +=[m]
    return jõr
