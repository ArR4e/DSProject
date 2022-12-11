def transponeeriK(maatriks):
    uus_maatriks = []
    uus = []
    
    for i in range(len(maatriks[0])-1, -1, -1):
        uus.clear()
        for j in range(len(maatriks)-1, -1, -1):
            uus.append(maatriks[j][i])
        uus_maatriks.append(uus.copy())
    return uus_maatriks

maatriks = [[2, 1, 1, 0],[4, 5, 7, 0], [5, 1, 0, 5]]
# transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])