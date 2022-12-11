def transponeeriK(maatriks):
    
    uus_maatriks = []
    for i in range(len(maatriks[0])):
        uus_maatriks.append([])
    for i in range(len(maatriks[0])):
        for j in range(len(maatriks)):
            uus_maatriks[i].append(maatriks[j][i])
    for el in uus_maatriks:
        el.reverse()
    uus_maatriks.reverse()
    
    try:
        for i in range(len(uus_maatriks)):
            uus_maatriks.remove([])
    except:
        return uus_maatriks
    return uus_maatriks
transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])