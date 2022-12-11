def transponeeriK(maatriks):
    for i in maatriks:
        b = len(i)
    transp_mat = []
    for x in range(b):
        transp_mat.append([])
    for x in transp_mat:
        for y in range(len(maatriks)):
            x.append(0)
    veerg = 0
    for i in range(len(maatriks)-1, -1, -1):
        rida = 0
        for j in range(b-1, -1, -1):
            transp_mat[rida][veerg] = maatriks[i][j]
            rida += 1
        veerg += 1
    
    return transp_mat

        
print(transponeeriK([[1, 2], [3, 4], [5, 6]]))
    