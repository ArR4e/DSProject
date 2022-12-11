def transponeeriK(maatriks):
    uus = []
    for i in maatriks:
        rida = []
        a = i[-1]
        for j in range(len(i[-1])):
            rida.append(j[-1])
        uus.append(rida)
    return uus