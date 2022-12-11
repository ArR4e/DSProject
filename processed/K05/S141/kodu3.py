def moos(suur, väike, kogus):
    
    if (5 * suur) + väike < kogus:
        return(-1)
    
    else:
        suured = int(kogus / 5)
        if suured > suur:
            suured = suur
        väiksed = kogus - suured * 5
        
        if väiksed > väike:
            return(-1)
        
        return(suured + väiksed)
   