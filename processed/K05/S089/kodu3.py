def moos(suuredkarbid_kogus, vaiksedkarbid_kogus, kilosid):
    suurkarp = 5
    vaikseidkarpe = kilosid % (suuredkarbid_kogus*suurkarp)
    suurikarpe = ((kilosid - vaikseidkarpe) / suurkarp)
    if vaikseidkarpe > vaiksedkarbid_kogus or suurikarpe > suuredkarbid_kogus:
        return(-1)
    else:        
        karpekokku = (suurikarpe + vaikseidkarpe)
        return(int(karpekokku))
    


