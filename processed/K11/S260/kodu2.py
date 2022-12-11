def transponeeriK(maatriks):
    maatriks_T = []
    for i in range(len(maatriks[0])):
        rida = []
        for j in range(len(maatriks)):
            rida.append(maatriks[len(maatriks)-1-j][len(maatriks[0])-1-i])
        maatriks_T.append(rida)
    return maatriks_T
    
print(transponeeriK([[4, 31, 67, 99]]))