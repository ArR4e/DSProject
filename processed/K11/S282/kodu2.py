def transponeeriK(maatriks):
    a=-1
    b=-1
    ridu=len(maatriks)
    if len(maatriks)>1:
        veerge=len(maatriks[0])
    else:
        veerge=1
    transponeeritud=[[0 for i in range(ridu)]for j in range(veerge)]
    if ridu==1 and veerge==1 :
        return maatriks
    else:
        for rida in maatriks:
            a+=1
            b=-1
            for veerg in rida:
                b+=1
                transponeeritud[-(b+1)][-(a+1)]=maatriks[a][b]
        return transponeeritud

