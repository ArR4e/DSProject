def transponeeriK(maatriks):
    transponeeritud = []
    for i in range(len(maatriks[0]),0,-1):
        elemendid = []
        for j in range(len(maatriks),0,-1):
            elemendid.append(maatriks[j-1][i-1])
        transponeeritud.append(elemendid)
    return transponeeritud



           