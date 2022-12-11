def transponeeriK(maatriks):
    uus = []
    for i in range(len(maatriks[0])-1,-1,-1):
        uusrida = []
        for j in range(len(maatriks)-1,-1,-1):
            uusrida.append(maatriks[j][i])
            
        uus.append(uusrida)
    return uus

