def transponeeriK(maatriks):
    uus = []
    tegemine = []
    x = 0
    for i in range(len(maatriks[0])-1,-1,-1):
        for j in range(len(maatriks)-1,-1,-1):
            tegemine.append(maatriks[j][i])
        uus.append(tegemine)
        tegemine = []
    return uus