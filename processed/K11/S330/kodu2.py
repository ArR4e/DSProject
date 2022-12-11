def transponeeriK(maatriks):
    tulemus = []
    for el in maatriks[0]:
        tulemus += [[""]]
    for rida in range(len(maatriks)-1):
        for i in range(len(tulemus)):
            tulemus[i] += [""]
    
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            tulemus[len(maatriks[i])-1-j][len(maatriks)-1-i] = maatriks[i][j]
    return tulemus