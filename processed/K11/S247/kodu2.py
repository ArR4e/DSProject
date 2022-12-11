def transponeeriK(maatriks):
    tühi = []
    for i in range(len(maatriks[0])-1, -1, -1):
        tühi1 = []
        for j in range(len(maatriks)-1, -1, -1):
            tühi1.append(maatriks[j][i])
        tühi.append(tühi1)
    return tühi
print(transponeeriK([[4, 31, 67, 99]]))

        