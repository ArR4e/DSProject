def transponeeriK(maatriks):
    
    mituRida = len(maatriks)
    mituVeergu = len(maatriks[0])
    
    transponeeritudMaatriks = []
    
    for v in range(0, mituVeergu):
        
        rida = []
        
        for r in range(0, mituRida):
            rida.append(maatriks[r][v])
        
        rida.reverse()
        
        transponeeritudMaatriks.append(rida)
       
    transponeeritudMaatriks.reverse()
    return transponeeritudMaatriks