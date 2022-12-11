def transponeeriK(maatriks):
    skirtaam = []
    for i in range(2, -1, -1):
        list = []
        for j in range(1, -1, -1):
            list.append(maatriks[j][i])
        skirtaam.append(list)  
    return skirtaam
