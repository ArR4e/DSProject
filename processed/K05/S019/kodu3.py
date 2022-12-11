def moos(s, v, kogus):
    
    karp = 0
    
    if kogus >= 5:
        karp += min(kogus // 5, s)
        kogus -= 5 * karp
    
    if kogus <= v:
        karp += kogus
        kogus -= kogus
    
    if kogus != 0:
         return -1
        
    return karp