def transponeeriK(maatriks):
    tulemus = [[0 for j in range(len(maatriks))] for i in range(len(maatriks[0]))]
    for j in range(len(maatriks), 0, -1):
        for i in range(len(maatriks[0]), 0, -1):
            tulemus[len(maatriks[0])-i][len(maatriks)-j] = maatriks[j-1][i-1]
    return tulemus