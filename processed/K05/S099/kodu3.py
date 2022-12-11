def moos(suur,väike,kogus):
    suured = 0
    väiksed = 0
    while kogus >= 5 and suured < suur:
        kogus -= 5
        suured += 1
    while kogus > 0 and väiksed < väike:
        kogus -= 1
        väiksed += 1
    if kogus == 0:
        return suured + väiksed
    else:
        return -1
    
moos(1,0,5)
        