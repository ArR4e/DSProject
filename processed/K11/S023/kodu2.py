


def transponeeriK(maatriks):
    uus_maatriks = []
    rida = []
    maatriks = maatriks[::-1]
    loendur = 0
    for i in range(len(maatriks[0])):
        for j in maatriks:
            j = j[::-1]
            for k in range(len(j)):
                if k == i:
                    rida.append(j[k])
        uus_maatriks.append(rida)
        loendur = loendur + 1
        rida = []
    return uus_maatriks
    
print(transponeeriK([[11, 12, 13, 14, 15, 16, 17, 18, 19], [21, 22, 23, 24, 25, 26, 27, 28, 29]]))

