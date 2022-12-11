def transponeeriK(maatriks):
    m = []
    for j in range(len(maatriks[0])-1,-1,-1):
        veerg = []
        for i in range(len(maatriks)-1,-1,-1):
                veerg.append(maatriks[i][j])
        m.append(veerg)
    return m

