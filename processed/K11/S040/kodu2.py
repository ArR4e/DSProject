def transponeeriK(x):
    x.reverse()
    maatriks = [[0 for j in range(len(x))] for i in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            maatriks[j][i] = x[i][j]
    maatriks.reverse()
    return maatriks