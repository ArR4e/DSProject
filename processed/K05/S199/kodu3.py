def moos(suured, väikesed, moos):
    kasutatud_suured = 0
    suuri_järel = suured
    kasutatud_väikesed = 0
    väikeseid_järel = väikesed
        
    while moos // 5 > 0 and suuri_järel > 0:
        moos -= 5
        kasutatud_suured += 1
        suuri_järel -= 1
    if moos == 0:
        return(kasutatud_suured)
    else:
        while moos > 0 and väikeseid_järel > 0:
            moos -= 1
            kasutatud_väikesed += 1
            väikeseid_järel -= 1
        if moos == 0:
            return(kasutatud_suured + kasutatud_väikesed)
        else:
            return(-1)
                

