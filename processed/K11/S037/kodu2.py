def transponeeriK(maatriks):
    if type(maatriks[0]) == int:
        maatriks.reverse()
        return maatriks
    maatriks.reverse()
    for rida in maatriks:
        rida = rida.reverse()
    a = 0
    uus_maatriks = []
    while a < len(maatriks):
        n = 0
        while len(maatriks[0]) > n:
            uus_maatriks += [maatriks[a][n]]
            n +=1
        a += 1
    l = 0
    transponeeritud = []
    while len(maatriks[0]) > l:
        transponeeritud += [uus_maatriks[::(len(maatriks[0]))]]
        uus_maatriks.remove(uus_maatriks[0])
        l +=1
    return transponeeritud
