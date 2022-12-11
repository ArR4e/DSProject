def moos(suured, vaikesed, mooskg):
    m = mooskg
    i = 0
    while m > 4 and suured > 0:
        m -= 5
        suured -= 1
        i += 1
    while m > 0 and vaikesed > 0:
        m -= 1
        vaikesed -= 1
        i += 1
    while m == 0:
        return i
    return -1

        
        
    
    
