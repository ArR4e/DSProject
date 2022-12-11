

def transponeeriK(maatriks):
    uus_maatriks = []
    for rida in maatriks:
        for el in rida:
            if len(uus_maatriks) < rida.index(el)+1:
                uus_maatriks.append([])
            uus_maatriks[rida.index(el)].append(el)
    
    for rida in uus_maatriks:
        rida = rida.reverse()
    MATRIX = list(reversed(uus_maatriks))
    
    return MATRIX
            
print(transponeeriK([[4, 31, 67, 99]]))