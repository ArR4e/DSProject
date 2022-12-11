def transponeeriK(maatriks):
    uus = []
    for i in range(len(maatriks[0])-1,-1,-1):
        tühi = []
        for j in range(len(maatriks)-1,-1,-1):
            tühi.append(maatriks[j][i])
        uus.append(tühi)
        
    return uus
    
  