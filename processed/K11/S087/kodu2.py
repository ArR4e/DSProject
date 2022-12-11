def transponeeriK(maatriks):
    transponeeritud_maatriks = []
    for i in range((len(maatriks[0])-1),-1,-1):
        vahetus = []
        for j in range((len(maatriks)-1),-1,-1):
            väärtus = maatriks[j][i]
            vahetus.append(väärtus)
        transponeeritud_maatriks.append(vahetus)
    return transponeeritud_maatriks