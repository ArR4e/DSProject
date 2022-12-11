def transponeeriK(maatriks):
    uusmaatriks = []
    
    pikkus = len(maatriks)
    laius = len(maatriks[0])
  
    for i in range((laius-1),-1,-1):
        uusrida = []
        for j in range((pikkus-1),-1,-1):
            uusrida.append(maatriks[j][i])
            
        uusmaatriks.append(uusrida)
    
    return uusmaatriks

