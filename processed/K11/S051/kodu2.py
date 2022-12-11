def transponeeriK(maatriks):
    trans_maatriks = []
    
    # uue maatriksi sama suureks tegemine
    for k in range(len(maatriks)):
        for l in range(len(maatriks[k])):
            if k == 0:
                trans_maatriks.append([])
                trans_maatriks[l] += "-"
            else:
                trans_maatriks[l].append("-")
    
    # transponeerimine
    for x in range(len(maatriks)):
        for y in range(len(maatriks[x])):
            v = maatriks[x][y]
            trans_maatriks[-(y+1)][-(x+1)] = v
    return trans_maatriks