def transponeeriK(mtr):
    uus = []
    
    for i in reversed(range(len(mtr[0]))):
        uus_mtr = []
        for j in range(len(mtr)-1,-1,-1):
            uus_mtr.append(mtr[j][i])
        uus.append(uus_mtr)
    return uus
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
