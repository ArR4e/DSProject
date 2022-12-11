def transponeeriK(maatriks):
    uus_maatriks = []
    read = len(maatriks)
    veerud = len(maatriks[0])
    
    for i in range(veerud):
        rida = []
        for j in range(read):
            rida.append(maatriks[j][i])
        rida.reverse()
        uus_maatriks.append(rida)
    uus_maatriks.reverse()
    return uus_maatriks
    
print(transponeeriK([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))
