def transponeeriK(mtrx):
    tulemus = []
    if len(mtrx) > len(mtrx[0]):
        for i in range(len(mtrx[0])):
            rida = mtrx[i]
            uusrida = []
            for j in range(len(mtrx)):
                reaelement = mtrx[j][i]
                uusrida.append(reaelement)
            uusrida.reverse()
            tulemus.append(uusrida)
        tulemus.reverse()
        return tulemus
    else:
        for i in range(len(mtrx[0])):
            uusrida = []
            for j in range(len(mtrx)):
                reaelement = mtrx[j][i]
                uusrida.append(reaelement)
            uusrida.reverse()
            tulemus.append(uusrida)
        tulemus.reverse()
        return tulemus