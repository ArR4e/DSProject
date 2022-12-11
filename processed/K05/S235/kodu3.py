def moos(suured_karbid, väiksed_karbid, kogus):
    kasutatud = 0
    while kogus >= 5 and suured_karbid >= 1:
        kasutatud += 1
        suured_karbid -= 1
        kogus -= 5
    if kogus == 0 or väiksed_karbid >= kogus:
        return(kasutatud + kogus)
    else:
        return(-1)