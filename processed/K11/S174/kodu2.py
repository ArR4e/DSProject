def transponeeriK(maatriks):
    transp_maatriks = []
    for i in range(len(maatriks[0])-1, -1, -1): #i tähistab rida
        transp_maatriks2 = []
        for j in range(len(maatriks)-1, -1, -1): #j tähistab veergu
            transp_maatriks2.append(maatriks[j][i])
        transp_maatriks.append(transp_maatriks2)
    return transp_maatriks

print(transponeeriK([[9, 6, 3], [8, 5, 2], [7, 4, 1]]))
