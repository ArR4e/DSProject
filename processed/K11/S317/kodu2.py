def transponeeriK(maatriks):
    uus = []
    väike = []
    pikkus1 = len(maatriks[0])
    pikkus2 = len(maatriks)
    for i in range(pikkus1-1,-1,-1):
        if [] in uus:
            uus.remove([])
        uus.append(väike)
        väike = []
        for j in range(pikkus2-1,-1,-1):
            väike.append(maatriks[j][i])
    uus.append(väike)
    if [] in uus:
        uus.remove([])
    return uus