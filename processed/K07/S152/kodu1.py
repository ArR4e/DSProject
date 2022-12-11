def poisse_ja_tüdrukuid(järjend):
    tühi =[]
    poiss = 0
    tüdruk = 0
    
    for inimene in järjend:
        uus=inimene[-1]  #viimane täht
        if uus == "P":
            poiss += 1
        if uus == "T":
            tüdruk += 1
        else:
            if järjend == tühi:
                return(0)
            
    return ((poiss, tüdruk))

      
    