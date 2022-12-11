def transponeeriK(maatriks):
    transp_m = []
    lisatav = []
    for rida in maatriks[0]:
        lisatav = []
        for i in maatriks:
            lisatav.append(0)
        transp_m.append(lisatav)
    for x in range(0,len(maatriks)):
        for y in range(0, len(maatriks[0])):
            transp_m[len(transp_m)-y-1][len(transp_m[0])-x-1] = maatriks[x][y]
    return(transp_m)

#print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))