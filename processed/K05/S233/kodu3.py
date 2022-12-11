def moos(suured,väiksed,kogus):
    karpe_kokku = 0
        
    while kogus >= 5 and suured != 0:
        kogus -= 5
        karpe_kokku += 1
        suured -= 1
    if kogus == 0:
        return karpe_kokku
    if väiksed >= kogus:
        return karpe_kokku + kogus
    else:
        return -1