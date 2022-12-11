def moos(suuredkarbid, vaikesedkarbid, kogus):
    karbid = 0
    while (kogus - 5 >= 0) and suuredkarbid > 0:
        suuredkarbid -= 1
        kogus -= 5
        karbid += 1
    if suuredkarbid >= 0 and kogus == 0:
        return karbid
    elif vaikesedkarbid >= kogus:
        while vaikesedkarbid >= kogus and vaikesedkarbid != 0 and kogus != 0:
            vaikesedkarbid -= 1
            kogus -= 1
            karbid += 1
        return karbid
    else:
        return -1
        

moos(2, 6, 14)
moos(3, 3, 8)
moos(1, 2, 10)
        