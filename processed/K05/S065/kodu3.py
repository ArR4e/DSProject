# 3. Moosi keetmine (5. kodutöö)

def moos(suur, väike, kogus):
    karbid = 0
    while True:
        if suur == 0:
            break
        if kogus >= 5:
            kogus -= 5
            suur -= 1
            karbid += 1
        if kogus < 5:
            break
            
    if kogus == 0:
        return karbid
    if väike >= kogus:
        karbid += kogus
        return karbid
    else:
        return - 1