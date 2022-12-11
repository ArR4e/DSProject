def moos(suured, väikesed, kogus):
    karbid = 0
    while kogus > 0:
        if kogus >= 5 and suured > 0:
            kogus -= 5
            suured -= 1
            karbid += 1
            continue
        elif kogus > 0 and väikesed > 0:
            kogus -= 1
            väikesed -= 1
            karbid += 1
            continue
        else:
            karbid = -1
            break
    return(karbid)