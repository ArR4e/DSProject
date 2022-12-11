def transponeeriK(maatriks):
    lõpp=[]
    for j in range(len(maatriks[0]),-1,-1,-1):
        tühi=[]
        for i in range(len(maatriks)-1,-1,-1):
            tühi.append(maatriks[i][j])
        lõpp.append(tühi)
        tühi=[]
    return lõpp