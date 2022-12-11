def transponeeriK(alg):
    j = len(alg)
    i = len(alg[0])
    lopp = []
    for x in range(i):
        lopp.append([])
        for y in range(j):
            lopp[x].append(0)
    for x in range(j):
        for y in range(i):
            lopp[(i-1-y)][j-1-x] = alg[x][y]

    return lopp


print(transponeeriK([[4, 31, 67, 99]]))





