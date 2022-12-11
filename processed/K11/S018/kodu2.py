def transponeeriK(maatr):
    transp = []
    for i in range(len(maatr[0])):
        transp.append([])
        for j in range(len(maatr)):
            transp[i].append(0)
    
    m = len(transp)-1
    for i in range(len(transp)):
        n = len(transp[0])-1
        for j in range(len(transp[0])):
            transp[i][j] = maatr[n][m]
            n -= 1
        m -= 1
    return transp