def transponeeriK (maatriks):
    maatriks2=[]
    veerge=len(maatriks)
    ridu=len(maatriks[0])
    for i in range(ridu-1,-1,-1):
        pane_juurde=[]
        for j in range(veerge-1,-1,-1):
            pane_juurde.append(maatriks[j][i])
        maatriks2.append(pane_juurde)
    return maatriks2
print(transponeeriK([[1,2,3],[4,5,6],[7,8,9]]))
            