def transponeeriK(maatriks):
    uus_maatriks = []
    for i in range(len(maatriks[0])-1,-1,-1):
        e_jär = []
        for j in range(len(maatriks)-1,-1,-1):
            e_jär.append(maatriks[j][i])
        uus_maatriks.append(e_jär)        
    return uus_maatriks
