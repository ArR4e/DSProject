def transporeeriK(maatriks):
    rida = len(maatriks)
    veerg = len(maatriks[0])

    maatriks_T = []
    for j in range(veerg):
        rida = []
        for i in range(rida):
            row.append(maatriks[i][j])
        maatriks_T.append(rida)
        
    return maatriks_T
transporeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])