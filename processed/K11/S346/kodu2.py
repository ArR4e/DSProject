def transponeeriK(maatriks):
    hulk = []
    for i in range(len(maatriks[0])):
        hulk.append(list())
        for j in range(len(maatriks)):
            hulk[i].append(maatriks[j][i])
    uus = []
    for i in hulk:
        i = i[::-1]
        uus.append(i)
    uus = uus[::-1]
    return uus
