def transponeeriK(maatriks):
    
    uus_maatriks = [] 
    
    ridade_arv = len(maatriks) -1
    tulpade_arv = len(maatriks[0]) -1
    
    
    for i in range(tulpade_arv, -1, -1):
        rida = []
        
        for j in range(ridade_arv, -1, -1):
            rida.append(maatriks[j][i])
        uus_maatriks.append(rida)
        
    
    return uus_maatriks
    










