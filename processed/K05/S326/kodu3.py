def moos(suured_karbid, väiksed_karbid, moos):
    kasutatud_karbid = 0
    while moos - 5 >= 0 and suured_karbid > 0:
        moos -= 5
        kasutatud_karbid += 1
        suured_karbid -= 1
    if moos == 0:
        return kasutatud_karbid
    elif väiksed_karbid >= moos:
        return kasutatud_karbid + moos
    else:
        return -1
