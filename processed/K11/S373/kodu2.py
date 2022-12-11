def transponeeriK(maatriks):
    kuju1 = []
    
    for i in range(len(maatriks[0])-1, -1, -1):
        kuju2 = []
        for j in range(len(maatriks)-1, -1, -1):
            kuju2.append(maatriks[j][i])
        kuju1.append(kuju2)
        
    return kuju1