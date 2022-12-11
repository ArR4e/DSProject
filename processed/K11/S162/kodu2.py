def transponeeriK(maatriks):
    uusmaatriks=[]
    veerge=len(maatriks)
    ridu=len(maatriks[0])
    #return veerge,ridu
    for i in range(ridu-1,-1,-1):
        lisa=[]
        for j in range(veerge-1,-1,-1):
            #print(maatriks[j][i],end=' ')
            lisa.append(maatriks[j][i])
        #print()
        uusmaatriks.append(lisa)
    return uusmaatriks
            #uusmaatriks[i][j]=maatriks[][]
print(transponeeriK([[4, 31, 67, 99]]))