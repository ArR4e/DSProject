# 2. Maatriksi transponeerimine kõrvaldiagonaali järgi

#maatriks = [[1, 2],
#            [3, 4],
#            [5, 6],
#            [7, 8]]

def transponeeriK(maatriks):
    transponeeritud = []
    i = len(maatriks[0]) - 1
    j = len(maatriks) - 1
    for rida in range(i,-1,-1):
        rida_uus = []
        for veerg in range(j,-1,-1):
            rida_uus += [maatriks[veerg][rida]]
        transponeeritud += [rida_uus]
    return transponeeritud

# print(transponeeriK(maatriks))