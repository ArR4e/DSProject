def transponeeriK(maatriks):
    uus = []
    i = len(maatriks[0]) - 1
    j = len(maatriks) - 1
    for rida in range(i, -1, -1):
        uusrida = []
        for el in range(j, -1, -1):
            uusrida += [maatriks[el][rida]]
        uus += [uusrida]
    return uus
