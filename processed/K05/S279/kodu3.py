def moos(suured, väikesed, kogus):
    uus_kogus = kogus
    kasutatud_suured = 0
    alles_suured = suured
    while uus_kogus >= 5 and suured > 0:
        uus_kogus -= 5
        kasutatud_suured += 1
        alles_suured -= 1
        if alles_suured > 0:
            continue
        else:
            break
    
    if väikesed >= uus_kogus:
        kasutatud_väikesed = uus_kogus
        return(kasutatud_suured + kasutatud_väikesed)
    else:
        return(-1)
