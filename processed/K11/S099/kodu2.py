def transponeeriK(maatriks):
    uus_maatriks = []
    for i in range(len(maatriks[0])):
        uus_rida = []
        for j in range(len(maatriks)):
            uus_rida.append(maatriks[-1-j][-1-i])
        uus_maatriks.append(uus_rida)
            
    return uus_maatriks

print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
