def moos(suur, väike, kg):
    karpe = 0
    if suur*5+väike < kg:
        return -1
    
    while kg >= 5 and suur > 0:
        kg -= 5
        suur -= 1
        karpe += 1
        
    while kg > 0 and väike > 0:
        kg = kg - 1
        väike -= 1
        karpe += 1
            
    if kg == 0:
        return karpe
        
    else:
        return -1
                
