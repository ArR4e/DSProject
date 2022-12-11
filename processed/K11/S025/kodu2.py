def transponeeriK(m):
    uus = []
    for i in range(len(m[0])-1, -1, -1):
        a = []
        for j in range(len(m)-1, -1, -1):
            a.append(m[j][i])
        uus.append(a)
    return uus