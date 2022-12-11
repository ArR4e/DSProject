def transponeeriK(a):
    pikkus = len(a)
    laius = len(a[0])
    ret = list()

    i = 0
    for x in range(0,laius):
        ret.append(list())
        for y in range(0,pikkus):
            ret[x].append(i)
            i+=1

    for x in range(0,pikkus):
        for y in range(0,laius):
            ret[laius-y-1][pikkus-x-1] = a[x][y]

    return ret