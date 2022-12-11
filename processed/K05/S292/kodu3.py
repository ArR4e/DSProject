def moos(suur, väike, kilod):
    suur = suur
    väike = väike
    kilod = kilod
    karbid = 0
    for karp in range(suur):
        if kilod-5 >= 0:
            karbid = karbid+1
            kilod = kilod - 5
    for karp in range(väike):
        if kilod-1 >= 0:
            karbid = karbid+1
            kilod = kilod - 1
    if kilod > 0:
        karbid = -1
    return karbid