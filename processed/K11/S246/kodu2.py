def transponeeriK(maatriks):
    transponeeritud = []
    el = maatriks[0]
    for i in range(len(el)-1, -1, -1):
        ajutine = []
        for j in range(len(maatriks)-1, -1, -1):
            muutuja = maatriks[j][i]
            ajutine.append(muutuja)
        transponeeritud.append(ajutine)
    return transponeeritud
print(transponeeriK([[1, 2, 7, 8]]))