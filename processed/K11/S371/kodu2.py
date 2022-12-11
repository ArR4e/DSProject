def transponeeriK(maatriks):
    uus_maatriks = []
    read = len(maatriks)
    veerud = len(maatriks[0])
    
    for i in range(veerud):
        elemendid = []
        for j in range(read):
            elemendid.append(maatriks[j][i])
        elemendid.reverse()
        uus_maatriks.append(elemendid)
    uus_maatriks.reverse()
    return uus_maatriks
print(transponeeriK([[4, 31, 67, 99]]))