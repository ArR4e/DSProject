def transponeeriK(maatriks):
    uus_maatriks = []
    uus_rida = []
    if len(maatriks) <= len(maatriks[0]):
        for i in range(len(maatriks[0]) - 1, -1, -1):
            uus_rida = []
            for j in range(len(maatriks) - 1 , -1, -1):
                uus_rida += [maatriks[j][i]]
            uus_maatriks += [uus_rida]
    elif len(maatriks) > len(maatriks[0]):
        for i in range(len(maatriks[0]) - 1, -1, -1):
            uus_rida = []
            for j in range(len(maatriks)-1, -1, -1):
                uus_rida += [maatriks[j][i]]
            uus_maatriks += [uus_rida]
    return uus_maatriks
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))