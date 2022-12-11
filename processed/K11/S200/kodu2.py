def transponeeriK(maatriks):
    uus = []
    pikkus = len(maatriks)
    
    if pikkus == 1:
            for j in range(len(maatriks[0])-1,-1, -1):
                teine = []
                teine.append((maatriks[0][j]))
                uus.append(teine)

    elif pikkus < len(maatriks[0]):
        for i in range(len(maatriks[0])-1,-1, -1):
            teine = []
            for j in range((pikkus)-1,-1, -1):
                teine.append((maatriks[j][i]))
            uus.append(teine)
    
    elif pikkus >= len(maatriks[0]):
        for i in range(len(maatriks[0])-1,-1, -1):
            teine = []
            for j in range((pikkus)-1,-1, -1):
                teine.append((maatriks[j][i]))
            uus.append(teine)
        
    
    
    return(uus)