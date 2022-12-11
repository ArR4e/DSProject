def transponeeriK(xd):
    counti = -1
    for i in xd:
        counti += 1
    countj = -1
    for j in xd[0]:
        countj += 1
    for i in range(1, len(xd[counti])):
        for j in range(1, len(xd[countj])):
            xd[i][j], xd[counti - j][countj - i] = xd[counti - j][countj - i], xd[i][j]
    return xd