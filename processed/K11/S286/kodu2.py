def transponeeriK(x):
    valmis = []
    for i in range(len(x[0])-1,-1,-1):
        vahepealne = []
        for j in range(len(x)-1,-1,-1):
            vahepealne.append(x[j][i])
        valmis.append(vahepealne)
    return valmis
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))