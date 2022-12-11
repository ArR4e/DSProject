def transponeeriK (maatriks):
    a = -1
    uus = []
    osa = []
    b = (len(maatriks)-1)
    while len(uus)< len(maatriks[0]):
        osa = []
        
        b = (len(maatriks)-1)
        for i in range(b+1):
            osa.append(maatriks[b][a])
            b = b - 1
        uus.append(osa)
        a = a-1
    return uus
(transponeeriK([[11, 12, 13, 14, 15, 16, 17, 18, 19], [21, 22, 23, 24, 25, 26, 27, 28, 29], [31, 32, 33, 34, 35, 36, 37, 38, 39]]))
        
    