def moos(suured_karbid, väiksed_karbid, kogus):
    kasutatud_karbid = 0
    while kogus >= 5 and suured_karbid > 0:
        kogus -= 5
        suured_karbid -= 1
        kasutatud_karbid += 1
    if kogus == 0:
        return kasutatud_karbid
    elif kogus > väiksed_karbid:
        return -1
    else:
        kasutatud_karbid += kogus
    return kasutatud_karbid