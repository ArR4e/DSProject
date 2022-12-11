def moos(suur, vaike, kogus):
    
    karpide_arv = 0
    
    while True:
        
        if 5 <= kogus and suur > 0:
            kogus -= 5
            suur -= 1
            karpide_arv += 1
        
        elif 1 <= kogus and vaike > 0:
            kogus -= 1
            vaike -= 1
            karpide_arv += 1
        
        elif kogus < 1 and kogus > 0 or kogus < 5 and kogus > 0 and vaike == 0 or kogus >= 5 and suur == 0 and vaike == 0:
            karpide_arv = -1
            break
        
        elif kogus == 0:
            break
    
    return karpide_arv

print(moos(4,3,19))