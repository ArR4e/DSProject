def transponeeriK(maatriks):
    transponeeritud=[]
    for i in range(len(maatriks[0])-1,-1, -1):
        a=[]
        for j in range(len(maatriks)-1, -1, -1):
            a.append(maatriks[j][i])
        transponeeritud.append(a)
    return transponeeritud