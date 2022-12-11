def transponeeriK(maatriks):
    
    transp = []
    ridu = len(maatriks)
    veerge = len(maatriks[0])
    
    for i in range(veerge-1, -1, -1):
        uus=[]
        for j in range(ridu-1, -1, -1):
            uus.append(maatriks[j][i])
        transp.append(uus)
        
    return transp
