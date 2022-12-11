def transponeeriK(maatriks):
    uus_maatriks = []
    
    for i in range(len(maatriks[0])-1,-1,-1):
        
        uus_maatriks.append([])
        for j in range(len(maatriks)-1,-1,-1):
            uus_maatriks[-1].append(maatriks[j][i])
    
    return uus_maatriks
        

