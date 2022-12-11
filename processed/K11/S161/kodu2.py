maatriks=[[4, 31, 67, 99]]
def transponeeriK(maatriks):
    uusmaatriks=[]
    uusmaatriksv=[]
    for i in range(len(maatriks[0])-1,-1,-1):
        for j in range(len(maatriks)-1,-1,-1):
            uusmaatriksv.append(maatriks[j][i])
        uusmaatriks.append(uusmaatriksv)
        uusmaatriksv=[]
    return uusmaatriks
print(transponeeriK(maatriks))
