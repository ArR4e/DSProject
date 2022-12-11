def transponeeriK(maatriks):
    uusmaatriks=[]
    veerge=len(maatriks[0])
    ridu=len(maatriks)
    for i in range(ridu,-1,-1):
        ridadeks=[]
        for j in range(veerge,ridu-1,-1):
            ridadeks.append(maatriks)
        uusmaatriks.append(ridadeks)
    return uusmaatriks      
print(transponeeriK([[1,2,3],
            [4,5,6]]))