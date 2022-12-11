def transponeeriK(maatriks):
    uus_maatriks = []
    vahe_maatriks = []
    i = 0
    j = 0
    for veerg in range(len(maatriks[0])-1, -1, -1):
        for rida in range(len(maatriks)-1, -1, -1):
            #uus_maatriks[rida][el] = maatriks[rida][el]
            vahe_maatriks.append(maatriks[rida][veerg])
        uus_maatriks.append(vahe_maatriks)
        vahe_maatriks = []
        j = 0
    return uus_maatriks

print(transponeeriK([[4, 31, 67, 99]]))            
    
