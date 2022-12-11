def moos(suuredkarbid, väiksedkarbid, kogus):
    karpe=0
    if kogus<=suuredkarbid*5+väiksedkarbid:
        while kogus-5>=0 and suuredkarbid>0:
            kogus-=5
            karpe+=1
            suuredkarbid-=1
        while kogus-1>=0 and väiksedkarbid>0:
            kogus-=1
            karpe+=1
            väiksedkarbid-=1
        return(karpe)
    else:
        return(-1)
    
moos(2, 6, 14)