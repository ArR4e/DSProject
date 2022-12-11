def moos(suured_karbid,väikesed_karbid,moosi_kogus):
    kokku_karbid = 0
    while moosi_kogus >= 5 and suured_karbid > 0:
        kokku_karbid += 1
        moosi_kogus -= 5
        suured_karbid -= 1
    if moosi_kogus == 0:
        return kokku_karbid
    elif moosi_kogus > väikesed_karbid:
        return -1
    else:
        kokku_karbid += moosi_kogus
    return(kokku_karbid)