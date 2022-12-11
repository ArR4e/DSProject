

def moos(suur, väike, kogus):
    karp_indeks = 0
    if suur == 0:
        if kogus < väike:
            return kogus
        else:
            return -1
            
    while kogus >= 5:
        kogus -= 5
        suur -= 1
        karp_indeks += 1
        if suur == 0:
            break
        
    if 0 <= kogus <= väike:
        return karp_indeks + kogus
    else:
        return -1
    
print(moos(2, 6, 10))
        