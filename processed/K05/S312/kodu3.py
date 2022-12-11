def moos(suur, väike, kogus):
    karpe = 0
    while (kogus - 5) >= 0 and suur > 0:
        suur = suur - 1
        kogus = kogus - 5
        karpe += 1
    if kogus == 0:
        return karpe
    if väike >= kogus:
        karpe = karpe + kogus
    else:
        karpe = -1
    return karpe
    
