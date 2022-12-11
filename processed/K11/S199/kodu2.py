def transponeeriK(maatriks):
    uus_maatriks = []
    for i in range(len(maatriks[0])-1, -1, -1):
        uus_maatriks.append([maatriks[0][i]])
    if len(maatriks) == 1:
        return uus_maatriks
    else:
        for i in range(1, len(maatriks)):     
            loendur = 0
            for j in range(len(maatriks[i])):
                n = len(maatriks)-1 -loendur
                uus_maatriks[n] = [maatriks[i][j]] + uus_maatriks[n]
                loendur += 1
    return(uus_maatriks)
    
    


