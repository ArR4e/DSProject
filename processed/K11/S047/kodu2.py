def transponeeriK(maatriks):
    
    uus_maatriks = []
    for i in range(len(maatriks[0])):
        osa_maatriks = []
        for rida in maatriks:
            osa_maatriks += [rida[i]]
        osa_maatriks.reverse()
        uus_maatriks += [osa_maatriks]
    uus_maatriks.reverse()
    return uus_maatriks

    
maatriks = [[4, 31, 67, 99]]
              
    
transponeeriK(maatriks)    
    
    
    
